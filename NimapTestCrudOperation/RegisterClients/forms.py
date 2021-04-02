from django import forms
from .models import User

class ClientRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields = ['clientname']
        widgets ={
            'clientname' : forms.TextInput(attrs={'class':'form-control'})
        }