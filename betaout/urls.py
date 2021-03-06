from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny

admin.site.site_header = "Betaout : Admin"
admin.site.site_title = "Betaout : Admin"

urlpatterns = [
    url(r'^', include_docs_urls(title='Elucidata API', permission_classes=(AllowAny,))),
    url('admin/', admin.site.urls),
    url('api/v1/bouncer/', include('bouncer.urls')),
]
