import datetime
import json

from django.views.generic import CreateView, ListView, View, DetailView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import Waybill, DriverTask
from .forms import WayBillForm, DriverTaskForm


class GetWayBills(ListView):
    context_object_name = 'waybills'
    model = Waybill
    template_name = 'primary_docs/waybills_list.html'


class GetWayBillDetail(DetailView):
    context_object_name = 'waybill'
    model = Waybill
    template_name = 'primary_docs/waybills_detail.html'


class NewWayBill(CreateView):
    form_class = WayBillForm
    template_name = 'primary_docs/waybill_new.html'
    success_url = '/docs/waybills/'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = json.loads(request.body.decode('utf-8'))
            data['author'] = request.user.pk
            tasks_list = []
            for task in data['tasks']:
                task_form = DriverTaskForm(task)
                if task_form.is_valid():
                    new_task = task_form.save()
                    tasks_list.append(new_task.pk)
            data['tasks'] = tasks_list
            form = WayBillForm(data)
            if form.is_valid():
                waybill = form.save()
                if waybill.is_completed:
                    waybill.complete()
                else:
                    waybill.car.available = False
                    waybill.car.save()
                return HttpResponse(self.success_url, status=201)
            else:
                return JsonResponse(form.errors, content_type='application/json', status=406)
        else:
            return JsonResponse('Не верный запрос!', status=405)


class EditWayBill(View):
    form_class = WayBillForm
    model = Waybill
    template_name = 'primary_docs/waybill_new.html'
    success_url = '/docs/waybills/'

    def get(self, request, pk, *args, **kwargs):
        waybill = get_object_or_404(Waybill, pk=pk)
        if not waybill.is_completed and request.user.is_staff:
            return render(request, self.template_name)
        else:
            msg = 'Недостаточно прав' if not request.user.is_staff else 'Путевой лист завершен'
            raise PermissionDenied(msg)

    def post(self, request, pk, *args, **kwargs):
        waybill = get_object_or_404(Waybill, pk=pk)
        if not waybill.is_completed and request.user.is_staff:
            if request.is_ajax:
                data = json.loads(request.body.decode('utf-8'))
                data['author'] = request.user.pk
                tasks_list = []
                for task in data['tasks']:
                    task_form = DriverTaskForm(task)
                    if task_form.is_valid():
                        new_task, created = DriverTask.objects.get_or_create(**task_form.cleaned_data)
                        tasks_list.append(new_task.pk)
                data['tasks'] = tasks_list
                form = WayBillForm(data, instance=waybill)
                if form.is_valid():
                    waybill = form.save()
                    if waybill.is_completed:
                        waybill.complete()
                    else:
                        waybill.car.available = False
                        waybill.car.save()
                    return HttpResponse(self.success_url, status=200)
                return JsonResponse(form.errors, content_type='application/json', status=409)
            else:
                return JsonResponse('Не верный запрос!', status=405)
        else:
            msg = 'Недостаточно прав' if not request.user.is_staff else 'Путевой лист завершен'
            raise PermissionDenied(msg)


def print_waybill(request, pk):
    waybill = get_object_or_404(Waybill, pk=pk)
    if waybill.is_completed:
        return render(request, waybill.get_template, {'wb': waybill})
    else:
        raise PermissionDenied('Путевой лист не завершен')





