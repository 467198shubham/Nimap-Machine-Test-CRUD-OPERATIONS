from django import forms
from .models import User
from .models import Projects

class ClientRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields = ['clientname']
        widgets ={
            'clientname' : forms.TextInput(attrs={'class':'form-control'})
        }
        
