from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
    url(r'^', include('registerApp.urls')),

	#Admin Urls
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
]