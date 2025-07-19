# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
from django import forms
from .models import Incident

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'reported_by', 'date', 'location', 'severity']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Incident Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detailed Description'}),
            'reported_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reported By'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Incident Location'}),
            'severity': forms.Select(attrs={'class': 'form-control'})
        }
