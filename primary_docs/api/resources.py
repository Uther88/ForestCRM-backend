import json
import datetime

from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, SessionAuthentication, ApiKeyAuthentication, MultiAuthentication, Authentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields
from django.db.models import Q

from taskmaster.api.resources import UserResource

from primary_docs import models
from primary_docs import forms as prd_forms

class OrganizationResource(ModelResource):
    head = fields.ForeignKey('primary_docs.api.resources.WorkerResource', 'head', full=True, null=True)

    class Meta:
        queryset = models.Organization.objects.all()
        resource_name = 'organizations'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'organizations'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())


class StationResource(ModelResource):
    organization = fields.ForeignKey(OrganizationResource, 'organization', full=True, null=True)
    head = fields.ForeignKey('primary_docs.api.resources.WorkerResource', 'head', full=True, null=True)
    masters = fields.ManyToManyField('primary_docs.api.resources.WorkerResource', 'masters', full=True, null=True)

    class Meta:
        queryset = models.Station.objects.all()
        resource_name = 'stations'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'stations'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'name': ALL,
            'organization': ALL_WITH_RELATIONS
        }


class UnitsResource(ModelResource):
    class Meta:
        queryset = models.Units.objects.all()
        resource_name = 'units'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'units'
        always_return_data = True
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'name': ALL,
            'short': ALL,
        }


class MaterialCategoryResource(ModelResource):
    class Meta:
        queryset = models.MaterialCategory.objects.all()
        resource_name = 'categories'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'categories'
        always_return_data = True
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'id': ALL,
            'name': ALL,
        }


class MaterialResource(ModelResource):
    category = fields.ForeignKey(MaterialCategoryResource, 'category', full=True)
    units = fields.ForeignKey(UnitsResource, 'units', full=True)

    class Meta:
        queryset = models.Material.objects.all()
        resource_name = 'materials'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        collection_name = 'materials'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'id': ALL,
            'name': ALL,
            'category': ALL_WITH_RELATIONS,
            'units': ALL_WITH_RELATIONS,
        }


class FuelResource(ModelResource):
    name = fields.ApiField('get_full')

    class Meta:
        queryset = models.Fuel.objects.all()
        resource_name = 'fuel'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        collection_name = 'fuels'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())


class CarResource(ModelResource):
    fuel = fields.ForeignKey(FuelResource, 'fuel', full=True, null=True)
    full_name = fields.ApiField('full_name')

    class Meta:
        queryset = models.Car.objects.all()
        resource_name = 'car'
        limit = 200
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        collection_name = 'cars'
        filtering = {
            'id': ALL,
            'kind': ALL,
            'name': ALL_WITH_RELATIONS,
            'number': ALL,
        }
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())


class WorkerResource(ModelResource):
    full_name = fields.ApiField('get_short_full_name')
    station = fields.ForeignKey(StationResource, 'station', null=True)
    position = fields.ApiField('get_position')

    class Meta:
        queryset = models.Worker.objects.all()
        resource_name = 'workers'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'workers'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        limit = 200
        filtering = {
            'id': ALL,
            'station': ALL_WITH_RELATIONS,
            'level': ALL,
        }

    def __str__(self):
        return '{} {}.{}.'.format(self.surname, self.name[0], self.patronymic[0])


class DriverTaskResource(ModelResource):
    customer = fields.ApiField('customer_id')
    car = fields.ApiField('car_id')
    conds_full = fields.ApiField('get_conditions_display')
    get_rate = fields.ApiField('get_rate')

    class Meta:
        queryset = models.DriverTask.objects.all()
        limit = 100
        resource_name = 'driver_task'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        collection_name = 'driver_tasks'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())


class OutfitEventResource(ModelResource):
    full_name = fields.ApiField('full_name')
    
    class Meta:
        queryset = models.OutfitEvent.objects.all()
        resource_name = 'outfit_events'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        collection_name = 'outfit_events'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        limit = 100


class WayBillResource(ModelResource):
    event = fields.ForeignKey(OutfitEventResource, 'event', full=True, null=True)
    tasks = fields.ToManyField(DriverTaskResource, 'tasks', full=True)
    driver = fields.ForeignKey(WorkerResource, 'driver', full=True)
    dispatcher = fields.ForeignKey(WorkerResource, 'dispatcher', full=True, null=True)
    car_took = fields.ForeignKey(WorkerResource, 'car_took', full=True)
    auto_accept = fields.ForeignKey(WorkerResource, 'auto_accept', full=True)
    auto_passed = fields.ForeignKey(WorkerResource, 'auto_passed', full=True)
    check_out_allow = fields.ForeignKey(WorkerResource, 'check_out_allow', full=True)
    car = fields.ForeignKey(CarResource, 'car', full=True)
    organization = fields.ForeignKey(OrganizationResource, 'organization', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    departament_full = fields.ApiField('get_departament_display')
    type_display = fields.ApiField('get_type_of_display')
    author = fields.ForeignKey(UserResource, 'author', full=True)
    fuel_distribution = fields.ForeignKey('primary_docs.api.resources.FuelDistributionResource', 'fuel_distribution', null=True)

    class Meta:
        queryset = models.Waybill.objects.all()
        limit = 100
        resource_name = 'waybill'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        collection_name = 'waybills'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'number': ALL,
            'date': ALL,
            'station': ALL_WITH_RELATIONS,
            'departament': ALL,
            'car': ALL_WITH_RELATIONS,
            'is_completed': ALL,
            'conducted': ALL,
            'driver': ALL_WITH_RELATIONS,
            'fuel_issued': ALL,
            'fuel_distribution': ALL_WITH_RELATIONS,
        }

    def put_detail(self, request, **kwargs):
        errors = []
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception as e:
            return self.error_response(request, e)
        if data.get('id'):
            try:
                waybill = models.Waybill.objects.get(id=data['id'])
            except Exception as e:
                return self.error_response(request, e)
            data['author'] = request.user.pk
            for task in data['tasks']:
                task['waybill'] = waybill.pk
                task_form = prd_forms.DriverTaskForm(task)
                if task_form.is_valid():
                    new_task, created = models.DriverTask.objects.get_or_create(**task_form.cleaned_data)
                else:
                    errors.append(task_form.errors)
            form = prd_forms.WayBillForm(data, instance=waybill)
            if form.is_valid():
                waybill = form.save()
                if waybill.is_completed:
                    waybill.complete()
                else:
                    waybill.car.available = False
                    waybill.car.save()
                return self.create_response(request, {'id': waybill.pk})
            else:
                errors.append(form.errors)
        return self.error_response(request, errors)

    def post_list(self, request, **kwargs):
        errors = []
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        form = prd_forms.WayBillForm(data)
        if form.is_valid():
            waybill = form.save()

            for task in data['tasks']:
                task['waybill'] = waybill.pk
                task_form = prd_forms.DriverTaskForm(task)
                if task_form.is_valid():
                    new_task = task_form.save()
                else:
                    errors.append(task_form.errors)

            if waybill.is_completed:
                waybill.complete()
            else:
                waybill.car.available = False
                waybill.car.save()
            return self.create_response(request, {'id': waybill.pk})
        else:
            errors.append(form.errors)
        return self.error_response(request, errors)


class OutfitWorkResource(ModelResource):
    units = fields.ForeignKey(UnitsResource, 'units', full=True)

    class Meta:
        queryset = models.OutfitWork.objects.all()
        resource_name = 'outfit_work'
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        collection_name = 'outfit_works'
        always_return_data = True
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())


class OutfitTableResource(ModelResource):
    worker = fields.ForeignKey(WorkerResource, 'worker', full=True)
    workdays = fields.DictField('workdays')

    class Meta:
        queryset = models.OutfitTable.objects.all()
        resource_name = 'outfit_table'
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        always_return_data = True
        collection_name = 'outfit_tables'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())


class OutfitResource(ModelResource):
    event = fields.ForeignKey(OutfitEventResource, 'event', full=True)
    works = fields.ToManyField(OutfitWorkResource, 'works', full=True)
    tables = fields.ToManyField(OutfitTableResource, 'tables', full=True)
    expenses = fields.ToManyField('primary_docs.api.resources.OutfitExpenseResource', 'expenses', full=True, null=True)
    postings = fields.ToManyField('primary_docs.api.resources.OutfitPostingResource', 'postings', full=True, null=True)
    brigadier = fields.ForeignKey(WorkerResource, 'brigadier', full=True)
    issued = fields.ForeignKey(WorkerResource, 'issued', full=True)
    accepted = fields.ForeignKey(WorkerResource, 'accepted', full=True)
    work_passed = fields.ForeignKey(WorkerResource, 'work_passed', full=True)
    work_accept = fields.ForeignKey(WorkerResource, 'work_accept', full=True)
    responsible = fields.ForeignKey(WorkerResource, 'responsible', full=True)
    calculated = fields.ForeignKey(WorkerResource, 'calculated', full=True)
    deposited = fields.ForeignKey(WorkerResource, 'deposited', full=True)
    organization = fields.ForeignKey(OrganizationResource, 'organization', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    departament_full = fields.ApiField('get_departament_display')
    quality_display = fields.ApiField('get_quality_display')
    recycling_list = fields.ForeignKey('primary_docs.api.resources.RecyclingListResource', 'recycling_list', null=True)
    act_spisanya = fields.ForeignKey('primary_docs.api.resources.ActSpisanyaResource', 'act_spisanya', null=True)
    fuel_distribution = fields.ForeignKey('primary_docs.api.resources.FuelDistributionResource', 'fuel_distribution', null=True)
    total_fuel = fields.ApiField('get_total_fuel')

    class Meta:
        queryset = models.Outfit.objects.all()
        resource_name = 'outfit'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        collection_name = 'outfits'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'id': ALL,
            'place': ALL,
            'date': ALL,
            'begin': ALL,
            'end': ALL,
            'event': ALL_WITH_RELATIONS,
            'brigadier': ALL_WITH_RELATIONS,
            'station': ALL_WITH_RELATIONS,
            'departament': ALL,
            'forestry': ALL,
            'conducted': ALL,
            'postings': ALL_WITH_RELATIONS,
            'expenses': ALL_WITH_RELATIONS,
            'recycling_list': ALL_WITH_RELATIONS,
            'total_fuel': ALL,
            'act_spisanya': ALL_WITH_RELATIONS,
            'fuel_distribution': ALL_WITH_RELATIONS,
        }

    def post_list(self, request, **kwargs):
        errors = []
        forms = dict(
            works=prd_forms.OutfitWorkForm,
            tables=prd_forms.OutfitTableForm,
            expenses=prd_forms.OutfitExpenseForm,
            postings=prd_forms.OutfitPostingForm
        )
        lists = dict(
            works=[],
            tables=[],
            expenses=[],
            postings=[],
        )

        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        data['organization'] = request.user.organization.pk
        outfit_form = prd_forms.OutfitForm(data)
        if outfit_form.is_valid():
            outfit = outfit_form.save()

            for lst in lists:
                for obj in data[lst]:
                    obj['outfit'] = outfit.pk
                    form = forms[lst](obj)
                    if form.is_valid():
                        form.save()
                    else:
                        errors.append(form.errors)
        else:
            errors.append(outfit_form.errors)

        if len(errors):
            return self.error_response(request, errors)
        return self.create_response(request, {'id': outfit.pk}) 
    
    def apply_filters(self, request, applicable_filters):
        filtered = super(OutfitResource, self).apply_filters(request, applicable_filters)
        if 'postings__isnull' in applicable_filters :
            filtered = filtered.distinct()
        if 'expenses__isnull' in applicable_filters :
            filtered = filtered.distinct()
        if 'gsm' in request.GET:
            if request.GET.get('gsm') == 'false':
                filtered = filtered.exclude(expenses__material__category__name='ГСМ')
            elif request.GET.get('gsm') == 'true':
                filtered = filtered.filter(expenses__material__category__name='ГСМ')
            filtered = filtered.distinct()
        return filtered
    

class OutfitExpenseResource(ModelResource):
    material = fields.ForeignKey(MaterialResource, 'material', full=True)
    outfit = fields.ForeignKey(OutfitResource, 'outfit')
    
    class Meta:
        queryset = models.OutfitExpense.objects.all()
        resource_name = 'outfit_expense'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'outfit_expenses'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'material': ALL_WITH_RELATIONS,
            'outfit': ALL_WITH_RELATIONS,
            'quantity_fact': ALL,
        }


class OutfitPostingResource(ModelResource):
    material = fields.ForeignKey(MaterialResource, 'material', full=True)
    outfit = fields.ForeignKey(OutfitResource, 'outfit')
    forest_arrival_reports = fields.ManyToManyField(
        'primary_docs.api.resources.ForestArrivalReportResource', 'forest_arrival_reports', null=True
        )

    class Meta:
        queryset = models.OutfitPosting.objects.all()
        resource_name = 'outfit_posting'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'outfit_postings'
        include_absolute_uri = True
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'material': ALL_WITH_RELATIONS,
            'outfit': ALL_WITH_RELATIONS,
            'forest_arrival_reports': ALL_WITH_RELATIONS,
        }


class TractorRegFormWorkResource(ModelResource):
    units = fields.ForeignKey(UnitsResource, 'units', full=True)

    class Meta:
        queryset = models.TractorRegFormWork.objects.all()
        resource_name = 'tractor-regform-work'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'works'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())


class TractorRegFormResource(ModelResource):
    event = fields.ForeignKey(OutfitEventResource, 'event', full=True)
    works = fields.ManyToManyField(TractorRegFormWorkResource, 'works', full=True)
    organization = fields.ForeignKey(OrganizationResource, 'organization', full=True)
    driver = fields.ForeignKey(WorkerResource, 'driver', full=True)
    car = fields.ForeignKey(CarResource, 'car', full=True)
    trailerman = fields.ForeignKey(WorkerResource, 'trailerman', full=True, null=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    brigadier = fields.ForeignKey(WorkerResource, 'brigadier', full=True)
    author = fields.ForeignKey(UserResource, 'author', full=True)
    departament_full = fields.ApiField('get_departament_display')
    fuel_distribution = fields.ForeignKey('primary_docs.api.resources.FuelDistributionResource', 'fuel_distribution', null=True)

    class Meta:
        queryset = models.TractorRegForm.objects.all()
        resource_name = 'tractor-regform'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'regforms'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'id': ALL,
            'date': ALL,
            'brigadier': ALL_WITH_RELATIONS,
            'driver': ALL_WITH_RELATIONS,
            'car': ALL_WITH_RELATIONS,
            'station': ALL_WITH_RELATIONS,
            'departament': ALL,
            'event': ALL_WITH_RELATIONS,
            'conducted': ALL,
            'fuel_distribution': ALL_WITH_RELATIONS,
        }

    def post_list(self, request, **kwargs):
        errors = []
        works_list = []
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        for work in data['works']:
            work_form = prd_forms.TractorRegFormWorkForm(work)
            if work_form.is_valid():
                new_work = work_form.save()
                works_list.append(new_work.pk)
            else:
                errors.append(work_form.errors)
        data['works'] = works_list
        form = prd_forms.TractorRegFormForm(data)
        if form.is_valid():
            tractor_regform = form.save()
            tractor_regform.car.update_data(fuel=tractor_regform.fuel_ret)
            return self.get_detail(request, **{'pk': tractor_regform.pk})
        else:
            errors.append(form.errors)
        if len(errors):
            return self.error_response(request, errors)


class SvodnayaZapisResource(ModelResource):
    waybill = fields.ForeignKey(WayBillResource, 'waybill', full=True)

    class Meta:
        queryset = models.SvodnayaZapis.objects.all()
        resource_name = 'svodnie_zapisi'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'svodnie_zapisi'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())


class SvodnayaVedomostResource(ModelResource):
    calcs = fields.ManyToManyField(SvodnayaZapisResource, 'calcs', full=True)
    author = fields.ForeignKey(UserResource, 'author', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    event = fields.ForeignKey(OutfitEventResource, 'event', full=True, null=True)
    departament_full = fields.ApiField('get_departament_display')


    class Meta:
        queryset = models.SvodnayaVedomost.objects.all()
        resource_name = 'svodnie_vedomosti'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'svodnie_vedomosti'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'id': ALL,
            'date': ALL,
            'created_date': ALL,
            'author': ALL_WITH_RELATIONS,
            'station': ALL_WITH_RELATIONS,
            'event': ALL_WITH_RELATIONS,
            'departament': ALL
        }

    def post_list(self, request, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        errors = []
        calcs_list = []
        for calc in data['calcs']:
            calc_form = prd_forms.SvodnayaZapisForm(calc['data'])
            if calc_form.is_valid():
                c = calc_form.save()
                c.waybill.conduct()
                calcs_list.append(c.pk)
            else:
                errors.append(calc_form.errors)
        data['calcs'] = calcs_list

        form = prd_forms.SvodnayaVedomostForm(data)
        if form.is_valid():
            sv = form.save()
        else:
            errors.append(form.errors)
        if not len(errors):
            return self.create_response(request, {'id': sv.pk})
        else:
            return self.error_response(request, errors)


class NakopitelnayaVedomostResource(ModelResource):
    regforms = fields.ManyToManyField(TractorRegFormResource, 'regforms', full=True, null=True)
    outfits = fields.ManyToManyField(OutfitResource, 'outfits', full=True, null=True)
    author = fields.ForeignKey(UserResource, 'author', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    event = fields.ForeignKey(OutfitEventResource, 'event', full=True, null=True)
    departament_full = fields.ApiField('get_departament_display')
    calcs = fields.ApiField('get_calcs_counter')

    class Meta:
        queryset = models.NakopitelnayaVedomost.objects.all()
        resource_name = 'nakopitelnie_vedomosti'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'nakopitelnie_vedomosti'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'id': ALL,
            'date': ALL,
            'created_date': ALL,
            'author': ALL_WITH_RELATIONS,
            'station': ALL_WITH_RELATIONS,
            'event': ALL_WITH_RELATIONS,
            'departament': ALL,
        }
        
    def post_list(self, request, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        errors = []
        calcs_list = []
        form = prd_forms.NakopitelnayaVedomostForm(data)
        if form.is_valid():
            vedomost = form.save()
            for of in vedomost.outfits.all():
                of.conducted = True
                of.save()
            for rf in vedomost.regforms.all():
                rf.conducted = True
                rf.save()
        else:
            errors.append(form.errors)
        if not len(errors):
            return self.create_response(request, {'id': vedomost.pk})
        else:
            return self.error_response(request, errors)


class WorkTimeEntryResource(ModelResource):
    worker = fields.ForeignKey(WorkerResource, 'worker', full=True)
    workdays = fields.DictField('workdays')

    class Meta:
        queryset = models.WorkTimeEntry.objects.all()
        resource_name = 'worktime_entries'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'worktime_entries'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'worker': ALL_WITH_RELATIONS
        }


class WorkTimeTableResource(ModelResource):
    entries = fields.ManyToManyField(WorkTimeEntryResource, 'entries', full_list=False, full=True, full_detail=True, null=True)
    outfits = fields.ManyToManyField(OutfitResource, 'outfits', full_list=False, full=True, full_detail=True, null=True)
    regforms = fields.ManyToManyField(TractorRegFormResource, 'regforms', full_list=False, full=True, full_detail=True, null=True)
    waybills = fields.ManyToManyField(WayBillResource, 'waybills', full_list=False, full=True, full_detail=True, null=True)
    author = fields.ForeignKey(UserResource, 'author', full=True)
    responsible = fields.ForeignKey(WorkerResource, 'responsible', full=True)
    performer = fields.ForeignKey(WorkerResource, 'performer', full=True)
    organization = fields.ForeignKey(OrganizationResource, 'organization', full=True, null=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    departament_full = fields.ApiField('get_departament_display')

    class Meta:
        queryset = models.WorkTimeTable.objects.all()
        resource_name = 'worktime_tables'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'worktime_tables'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'id': ALL,
            'date': ALL,
            'created_date': ALL,
            'author': ALL_WITH_RELATIONS,
            'station': ALL_WITH_RELATIONS,
            'departament': ALL,
        }
        
    def post_list(self, request, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        errors = []
        form = prd_forms.WorkTimeTableForm(data)
        if form.is_valid() and data.get('__entries', None):
            table = form.save()
            for entry_data in data['__entries']:
                entry_form = prd_forms.WorkTimeEntryForm(entry_data)
                if entry_form.is_valid():
                    entry = entry_form.save()
                    table.entries.add(entry.pk)
                else:
                    errors.append(form.errors)
        else:
            errors.append(form.errors)

        if not len(errors) and data.get('__entries', None):
            table.save()
            return self.create_response(request, {'id': table.pk})
        else:
            return self.error_response(request, errors)


class ForestArrivalReportResource(ModelResource):
    author = fields.ForeignKey(UserResource, 'author', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    postings = fields.ManyToManyField(OutfitPostingResource, 'postings', full=True, null=True)

    class Meta:
        queryset = models.ForestArrivalReport.objects.all()
        resource_name = 'forest-arrival-reports'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'reports'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'station': ALL_WITH_RELATIONS,
            'postings': ALL_WITH_RELATIONS,
            'author': ALL_WITH_RELATIONS,
            'date': ALL,
        }

    def post_list(self, request, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        form = prd_forms.ForestArrivalReportForm(data)
        if form.is_valid():
            report = form.save()
            return self.create_response(request, {'id': report.pk})
        else:
            return self.error_response(request, form.errors)


class RecyclingListResource(ModelResource):
    author = fields.ForeignKey(UserResource, 'author', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    outfits = fields.OneToManyField(OutfitResource, 'outfits', full=True, null=True)

    class Meta:
        queryset = models.RecyclingList.objects.all()
        resource_name = 'recycling-lists'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        collection_name = 'lists'
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'station': ALL_WITH_RELATIONS,
            'outfits': ALL_WITH_RELATIONS,
            'author': ALL_WITH_RELATIONS,
            'date': ALL,
        }

    def post_list(self, request, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        form = prd_forms.RecyclingListForm(data)
        if form.is_valid():
            recycling_list = form.save()
            for outfit_id in data['outfits']:
                recycling_list.outfits.add(models.Outfit.objects.get(pk=outfit_id))
            return self.create_response(request, {'id': recycling_list.pk})
        return self.error_response(request, form.errors)


class HandoutResource(ModelResource):
    author = fields.ForeignKey(UserResource, 'author', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    car = fields.ForeignKey(CarResource, 'car', full=True)
    worker = fields.ForeignKey(WorkerResource, 'worker', full=True)
    waybills = fields.ToManyField(WayBillResource, 'waybills', full=True)

    class Meta:
        queryset = models.Handout.objects.all()
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'handouts'
        collection_name = 'handouts'
        always_return_data = True
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'station': ALL_WITH_RELATIONS,
            'car': ALL_WITH_RELATIONS,
            'worker': ALL_WITH_RELATIONS,
            'waybills': ALL_WITH_RELATIONS,
            'author': ALL_WITH_RELATIONS,
            'date': ALL,
        }

    def post_list(self, request, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        form = prd_forms.HandoutForm(data)
        if form.is_valid() and data.get('waybills') and len(data.get('waybills')):
            handout = form.save()
            for wb in data['waybills']:
                handout.waybills.add(models.Waybill.objects.get(pk=wb))
            return self.create_response(request, {'id': handout.pk})
        return self.error_response(request, form.errors)
            

class FuelDistributionResource(ModelResource):
    author = fields.ForeignKey(UserResource, 'author', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    car = fields.ForeignKey(CarResource, 'car', full=True, null=True)
    worker = fields.ForeignKey(WorkerResource, 'worker', full=True)
    waybills = fields.ToManyField(WayBillResource, 'waybills', full_list=False, full=True, full_detail=True, null=True)
    outfits = fields.ToManyField(OutfitResource, 'outfits', full_list=False, full=True, full_detail=True, null=True)
    regforms = fields.ToManyField(TractorRegFormResource, 'regforms', full_list=False, full=True, full_detail=True, null=True)
    kind_full = fields.ApiField('get_kind_display')

    class Meta:
        queryset = models.FuelDistribution.objects.all()
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'fuel-distributions'
        collection_name = 'fuel_distributions'
        always_return_data = True
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'station': ALL_WITH_RELATIONS,
            'car': ALL_WITH_RELATIONS,
            'worker': ALL_WITH_RELATIONS,
            'waybills': ALL_WITH_RELATIONS,
            'outfits': ALL_WITH_RELATIONS,
            'regforms': ALL_WITH_RELATIONS,
            'author': ALL_WITH_RELATIONS,
            'date': ALL,
        }

    def post_list(self, request, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        form = prd_forms.FuelDistributionForm(data)
        if form.is_valid() and data.get('documents'):
            fuel_distribution = form.save()
            if fuel_distribution.kind == 'WB':
                for waybill in data['documents']:
                    fuel_distribution.waybills.add(models.Waybill.objects.get(pk=waybill))
            elif fuel_distribution.kind == 'OF':
                for outfit in data['documents']:
                    fuel_distribution.outfits.add(models.Outfit.objects.get(pk=outfit))
            elif fuel_distribution.kind == 'TR':
                for regform in data['documents']:
                    fuel_distribution.regforms.add(models.TractorRegForm.objects.get(pk=regform))

            return self.create_response(request, {'id': fuel_distribution.pk})

        return self.error_response(request, form.errors)


class ActSpisanyaResource(ModelResource):
    author = fields.ForeignKey(UserResource, 'author', full=True)
    organization = fields.ForeignKey(OrganizationResource, 'organization', full=True)
    station = fields.ForeignKey(StationResource, 'station', full=True)
    outfit = fields.ToOneField(OutfitResource, 'outfit', full_list=False, full=True, full_detail=True, null=True)
    comission = fields.ManyToManyField(WorkerResource, 'comission', full_list=False, full=True, full_detail=True)

    class Meta:
        queryset = models.ActSpisanya.objects.all()
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'act-spisanya'
        collection_name = 'acts'
        always_return_data = True
        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), ApiKeyAuthentication())
        filtering = {
            'organization': ALL_WITH_RELATIONS,
            'author': ALL_WITH_RELATIONS,
            'station': ALL_WITH_RELATIONS,
            'outfit': ALL_WITH_RELATIONS,
            'date': ALL,
        }

    def post_list(self, request, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        data['author'] = request.user.pk
        form = prd_forms.ActSpisanyaForm(data)
        if form.is_valid():
            act = form.save()
            return self.create_response(request, {'id': act.pk})
        return self.error_response(request, form.errors)