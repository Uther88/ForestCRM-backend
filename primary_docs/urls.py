from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import views

from tastypie.api import Api

from .api import resources

v1_api = Api(api_name='v1')
v1_api.register(resources.OrganizationResource())
v1_api.register(resources.StationResource())
v1_api.register(resources.UnitsResource())
v1_api.register(resources.CarResource())
v1_api.register(resources.WorkerResource())
v1_api.register(resources.WayBillResource())
v1_api.register(resources.OutfitEventResource())
v1_api.register(resources.OutfitResource())
v1_api.register(resources.TractorRegFormWorkResource())
v1_api.register(resources.TractorRegFormResource())
v1_api.register(resources.SvodnayaZapisResource())
v1_api.register(resources.SvodnayaVedomostResource())
v1_api.register(resources.NakopitelnayaVedomostResource())
v1_api.register(resources.WorkTimeEntryResource())
v1_api.register(resources.WorkTimeTableResource())
v1_api.register(resources.MaterialCategoryResource())
v1_api.register(resources.MaterialResource())
v1_api.register(resources.ForestArrivalReportResource())
v1_api.register(resources.OutfitPostingResource())
v1_api.register(resources.OutfitExpenseResource())
v1_api.register(resources.RecyclingListResource())
v1_api.register(resources.HandoutResource())
v1_api.register(resources.FuelDistributionResource())
v1_api.register(resources.ActSpisanyaResource())


urlpatterns = [

]