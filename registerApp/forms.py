# appname/forms.py
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from registerApp.models import CustomUser

from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError

class SignupForm(forms.Form):        
    email = forms.EmailField(label='Email', required=True) 
    plan = forms.CharField(label='Plan', required=True)    
    first_name = forms.CharField(label='first name', required=True)
    last_name = forms.CharField(label='last name', required=True)  

    def clean(self):

        if self.cleaned_data.get('plan') != 'Free' and self.cleaned_data.get('plan') != 'Gold' and self.cleaned_data.get('plan') != 'Platinum':

            raise ValidationError(
                "Invalid Plan value entered"
            )

        return self.cleaned_data

    class Meta:
        model = get_user_model()       

    def save(self, user):
        try:
            user.email = self.cleaned_data['email']
            user.plan = self.cleaned_data['plan']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.save()
        except ValidationError:
            return 'Invalid Plan value entered'

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        # del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        # del self.fields['username']

    class Meta:
        model = CustomUser
        fields = "__all__" 
