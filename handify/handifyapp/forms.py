from django import forms
from handifyapp.models import *

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserTable
        fields = ['Name','Email','Gender','Age']