from django.conf.urls import include, url
from registerApp.views import *
import allauth
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    url(r'^$', customRegister.as_view()),
    url(r'^login/$', customLogin.as_view()),
    url(r'^logout/$', customLogout.as_view()),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^dashboard/$', dashboard , name = 'dashboard'),
    url(r'^success/$', login_required(successView.as_view()), name = 'success'),
  
]