from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings

from allauth.account.views import *

from django.contrib.auth import get_user_model

from registerApp.models import Order

import requests
import json



User = get_user_model()

@login_required
def dashboard(req):
    return render(req,'dashboard.html', {'RAZOR_KEY_ID' : settings.RAZOR_KEY_ID})


class customRegister(SignupView):
    def __init__(self, **kwargs):
        super(customRegister, self).__init__(*kwargs)        
 
    def get_context_data(self, **kwargs):
        ret = super(customRegister, self).get_context_data(**kwargs)
        ret['signupform'] = get_form_class(app_settings.FORMS, 'signup', self)
        return ret	


class customLogin(LoginView):
    def __init__(self, **kwargs):
        super(customLogin, self).__init__(*kwargs)        
 
    def get_context_data(self, **kwargs):
        ret = super(customLogin, self).get_context_data(**kwargs)
        ret['loginform'] = get_form_class(app_settings.FORMS, 'login',self)
        return ret	 


class customEmailVerify(ConfirmEmailView):
    def __init__(self, **kwargs):
        super(customEmailVerify, self).__init__(*kwargs)        
    
    def get_context_data(self, **kwargs):
        ret = super(customEmailVerify, self).get_context_data(**kwargs)
        ret['verifyform'] = get_form_class(app_settings.FORMS, 'verify',self)
        print 'aloo'
        print ret
        return ret                  


class customLogout(LogoutView):
    def __init__(self, **kwargs):
        super(customLogout, self).__init__(*kwargs)        
 
    def get_context_data(self, **kwargs):
        ret = super(customLogout, self).get_context_data(**kwargs)
        ret['logoutform'] = get_form_class(app_settings.FORMS, 'logout',self)
        return ret	        

class successView(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, **kwargs):
        context = super(successView, self).get_context_data(**kwargs)
        txn_id = self.request.GET.get('txn_id')
        url = 'https://api.razorpay.com/v1/payments/%s/capture' % str(txn_id)
        resp = requests.post(url, data={'amount':200000}, auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        if resp.status_code == 200:
            order = Order()
            order.email = self.request.user
            order.payment_success = True
            order.transaction_details = str(resp.content)
            order.save()    
            context['status'] = 'Payment successful'
            return context
        elif resp.status_code == 400:
            order = Order()
            order.email = self.request.user
            order.payment_success = False
            order.transaction_details = str(resp.content)
            order.save()   
            context['status'] = 'Invalid amount passed'
            return context
        else:
            order = Order()
            order.email = self.request.user
            order.payment_success = False
            order.transaction_details = str(resp.content)
            order.save()
            context['status'] = 'Unauthorized access'
            return context   

