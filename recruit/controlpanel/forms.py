from django.forms import ModelForm
from .models import Applications
from django import forms

class ApplicationForm(ModelForm):
	class Meta:
		model = Applications
		fields = ["ref_id", "name", "email", "date_of_birth", "gender", "education", "profile"]
		widgets = {
		    'ref_id': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
		    'name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
		    'email': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
		    'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
		    'gender': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
		    'education': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
		    'profile': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
		}
		