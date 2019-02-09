from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from tastypie.api import Api
from .api.resources import TaskResource, UserResource,  MessageResource, FileResource, BugReportResource, ChatResource


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(TaskResource())
v1_api.register(MessageResource())
v1_api.register(ChatResource())
v1_api.register(FileResource())
v1_api.register(BugReportResource())


urlpatterns = [
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
