from django.contrib import admin

from . import models


class CarAdmin(admin.ModelAdmin):
    list_display = (
    	'name', 'number', 'fuel_balance', 'mileage',
    	'rate_normal_s', 'rate_normal_w',
    	'rate_hard_s', 'rate_hard_w'
    	)
    list_display_links = ('name',)
    list_filter = ('station', 'kind')
    search_fields = ('name', 'number',)
    list_per_page = 100


class MaterialAdmin(admin.ModelAdmin):
    list_display = (
    	'name', 'category', 'units', 'quantity',
    	)
    list_display_links = ('name',)
    list_filter = ('category',)
    search_fields = ('name',)
    list_per_page = 100


class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'position', 'station',
        )
    list_filter = ('station', 'position', 'level',)
    search_fields = ('surname', 'name', 'patronymic',)
    list_per_page = 100


admin.site.register(models.Organization)
admin.site.register(models.Station)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Worker, WorkerAdmin)
admin.site.register(models.Position)
admin.site.register(models.DriverTask)
admin.site.register(models.Waybill)
admin.site.register(models.Fuel)
admin.site.register(models.OutfitTable)
admin.site.register(models.Outfit)
admin.site.register(models.OutfitExpense)
admin.site.register(models.OutfitPosting)
admin.site.register(models.OutfitWork)
admin.site.register(models.OutfitEvent)
admin.site.register(models.TractorRegFormWork)
admin.site.register(models.TractorRegForm)
admin.site.register(models.SvodnayaZapis)
admin.site.register(models.SvodnayaVedomost)
admin.site.register(models.NakopitelnayaVedomost)
admin.site.register(models.WorkTimeTable)
admin.site.register(models.WorkTimeEntry)
admin.site.register(models.MaterialCategory)
admin.site.register(models.Material, MaterialAdmin)
admin.site.register(models.ForestArrivalReport)
admin.site.register(models.RecyclingList)
admin.site.register(models.Handout)
admin.site.register(models.FuelDistribution)
admin.site.register(models.ActSpisanya)
admin.site.register(models.Units)
