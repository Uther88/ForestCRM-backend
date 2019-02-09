
from django.conf.urls import url, include
from django.contrib import admin

from primary_docs.urls import v1_api as pd_api
from taskmaster.urls import v1_api as tm_api


urlpatterns = [
    url(r'^api/', include(tm_api.urls)),
    url(r'^api/', include(pd_api.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'', include('taskmaster.urls')),
]
