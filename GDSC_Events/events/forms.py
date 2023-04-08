from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email','phone']
        labels = {
            'name': 'Your name',
            'email': 'Your email address',
            'phone': 'Your phone number',
        }
