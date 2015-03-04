from django.conf.urls import patterns, include, url
from django.contrib import admin

from api.api import router
from api import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/', include(router.urls)), 
    url(r'^api-explorer/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
