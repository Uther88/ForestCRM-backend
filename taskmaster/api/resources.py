import json
import datetime

from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, SessionAuthentication, ApiKeyAuthentication, MultiAuthentication, Authentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.models import create_api_key

from django.db.models import Q, signals

from taskmaster.forms import TaskForm, UserForm
from taskmaster.models import User, Task, Message, File, BugReport, Chat


signals.post_save.connect(create_api_key, sender=User)


class UserResource(ModelResource):
    full_name = fields.ApiField('get_full_name')
    station = fields.ForeignKey('primary_docs.api.resources.StationResource', 'station', full=True, null=True)
    organization = fields.ForeignKey('primary_docs.api.resources.OrganizationResource', 'organization', full=True, null=True)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        allowed_methods = ['get', 'post', 'delete', 'put', 'options']
        authorization = Authorization()
        authentication = MultiAuthentication(ApiKeyAuthentication(), BasicAuthentication(),)
        collection_name = 'users'
        detail_uri_name = 'username'
        fields = (
            'username', 'id', 'full_name', 'first_name', 'last_name',
            'third_name', 'position', 'avatar', 'is_staff', 'email',
            )
        filtering = {
            'id': ('exact', 'ne',),
        }

    def dehydrate_avatar(self, bundle, **kwargs):
    	url = bundle.request.build_absolute_uri(bundle.obj.avatar.url)
    	return url

    def dehydrate(self, bundle):
        if bundle.request.GET.get('auth'):
            if bundle.obj == bundle.request.user:
                bundle.data['api_key'] = bundle.request.user.api_key.key
        return bundle

    def post_list(self, request, **kwargs):
        form = UserForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
        else: 
            return self.error_response(request, form.errors)

    def put_list(self, request, **kwargs):
        pk = request.GET.get('pk')
        if pk:
            try:
                instance = User.objects.get(pk=pk)
            except Exception as e:
                return self.error_response(request, e)
            if request.user.pk == instance.pk or request.user.is_staff:
                form = UserForm(request.POST or None, request.FILES or None, instance=instance)
                if form.is_valid():
                    user = form.save()
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    return user
                else:
                    return self.error_response(request, form.errors)
            return self.error_response(request, 'Не достаточно прав!')

class FileResource(ModelResource):
    sender = fields.ForeignKey(UserResource, 'sender', full=True)
    recipient = fields.ManyToManyField(UserResource, 'recipient', full=True)

    class Meta:
        queryset = File.objects.all()
        resource_name = 'files'
        allowed_methods = ['get', 'post', 'delete', 'patch']
        collection_name = 'files'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            "title": ALL,
            'sender': ALL_WITH_RELATIONS,
            'recipient': ALL_WITH_RELATIONS,
        }

    def dehydrate_file(self, bundle, **kwargs):
    	file_url = bundle.request.build_absolute_uri(bundle.obj.file.url)
    	return file_url


class MessageResource(ModelResource):
    sender = fields.ForeignKey(UserResource, 'sender', full=True)
    recipient = fields.ManyToManyField(UserResource, 'recipient', full=True)
    files = fields.ManyToManyField(FileResource, 'files', full=True)
    chats = fields.ManyToManyField('taskmaster.api.resources.ChatResource', 'chats')

    class Meta:
        queryset = Message.objects.all()
        resource_name = 'messages'
        allowed_methods = ['get', 'post', 'delete', 'patch']
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        collection_name = 'messages'
        always_return_data = True
        filtering = {
            "slug": ('exact', 'startswith',),
            "title": ALL,
            'is_new': ALL,
            'sender': ALL_WITH_RELATIONS,
            'recipient': ALL_WITH_RELATIONS,
            'chats': ALL_WITH_RELATIONS
        }

    def post_list(self, request, **kwargs):
        message = Message.objects.create(
            title=request.POST.get('title'),
            text=request.POST.get('text'),
            sender=request.user,
            )
        recipients = request.POST.getlist('recipient')
        for rec in recipients:
            message.recipient.add(rec)

        files = request.FILES.getlist('files', None)
        if files:
            for file in files:
                f = File.objects.create(sender=request.user, title=file.name, file=file)

                for recipient in message.recipient.all():
                    f.recipient.add(recipient)
                message.files.add(f)
        message.save()

        chat, created = Chat.objects.filter(members__id=request.user.id).get_or_create(members__in=recipients)
        if created:
            chat.members.add(request.user.id)
            for rec in message.recipient.all():
                chat.members.add(rec.id)
        chat.messages.add(message)
        chat.updated = message.created_date
        chat.save()
        return self.get_detail(request, **{'pk': message.pk})

    def apply_filters(self, request, applicable_filters):
        filtered_messages = super(MessageResource, self).apply_filters(request, applicable_filters)
        if request.GET.get('chats', None):
            for message in filtered_messages:
                if message.sender != request.user:
                    message.read()
        return filtered_messages


class ChatResource(ModelResource):
    members = fields.ManyToManyField(UserResource, 'members', full=True)
    messages = fields.ToManyField(
        MessageResource,  
        full=True, related_name="chats",
        attribute=lambda bundle: Message.objects.filter(chats=bundle.obj)[:1]
        )

    class Meta:
        queryset = Chat.objects.all()
        resource_name = 'chats'
        allowed_methods = ['get', 'post', 'delete', 'patch']
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        collection_name = 'chats'
        always_return_data = True
        filtering = {'messages': ALL_WITH_RELATIONS, 'members': ALL_WITH_RELATIONS}

    def get_object_list(self, request):
    	return Chat.objects.filter(members__id=request.user.id)


class TaskResource(ModelResource):
    performer = fields.ForeignKey(UserResource, 'performer', full=True)
    assigner = fields.ForeignKey(UserResource, 'assigner', full=True)
    files = fields.ManyToManyField(FileResource, 'files', full=True)

    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        collection_name = 'tasks'
        filtering = {
            "slug": ('exact', 'startswith'),
            "title": ALL,
            'is_completed': ALL,
            'assigner': ALL_WITH_RELATIONS,
            'performer': ALL_WITH_RELATIONS,
            'to_complete': ALL,
            'viewed': ALL
        }
    def post_list(self, request, **kwargs):
        errors = []
        form = TaskForm(request.POST or None)
        files = request.FILES.getlist('files', None)
        if form.is_valid():
            task = form.save()
            task.assigner = request.user

            if files:
                for file in files:
                    f = File.objects.create(sender=request.user, title=file.name, file=file)
                    f.recipient.add(task.performer)
                    task.files.add(f)
            task.save()
        else:
            return self.error_response(request, form.errors)

    def put_detail(self, request, **kwargs):
        try:
            data = json.loads(request.body.decode())
        except Exception as e:
            return self.error_response(request, e)
        else:
            if data.get('is_completed') and kwargs.get('pk'):
                task = Task.objects.get(pk=kwargs.get('pk'))
                if not task.is_completed and task.performer.id == request.user.id:
                    if data.get('comment') and data.get('comment') != '':
                        task.comment = data.get('comment')
                    task.complete()
                    
            elif data.get('viewed') and kwargs.get('pk'):
                task = Task.objects.get(pk=kwargs.get('pk'))
                if not task.viewed and task.performer.id == request.user.id:
                    task.viewed = True
                    task.save()

    def authorized_read_detail(self, object_list, bundle):
        if bundle.request.user.is_staff:
            return object_list.get(pk=bundle.obj.pk)
        else:
            object_list = object_list.filter(Q(assigner=bundle.request.user) | Q(performer=bundle.request.user))
            return object_list.get(pk=bundle.obj.pk)

    def authorized_read_list(self, object_list, bundle):
        if bundle.request.user.is_staff:
            return object_list.all()
        else:
            return object_list.filter(Q(assigner=bundle.request.user) | Q(performer=bundle.request.user))


class BugReportResource(ModelResource):
    reporter = fields.ForeignKey(UserResource, 'reporter', full=True)
    class Meta:
        queryset = BugReport.objects.all()
        resource_name = 'bug-reports'
        allowed_methods = ['get', 'post']
        collection_name = 'bug-reports'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
    