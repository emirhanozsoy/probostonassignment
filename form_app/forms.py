from django import forms
from .models import Form_Info

class AppForm(forms.ModelForm):
    class Meta:
        model= Form_Info
        fields = ['name', 'email','ico']
        widgets={
            'name': forms.TextInput(),
            'email': forms.TextInput(),
            'ico': forms.TextInput()
        }
  