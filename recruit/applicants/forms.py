from django import forms
from django.core.validators import validate_email

EDUCATION_CHOICES = (('BE', 'BE'), ('B-Tech', 'B-Tech'), ('BCA', 'BCA'))
GENDER_CHOICES = (('male', 'Male'), ('female', 'Female'))

class Application(forms.Form):
	"""docstring for Application"""
	name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={"class": "form-control"}))
	mobile = forms.IntegerField(label='Mobile', widget=forms.TextInput(attrs={"class": "form-control"}))
	date_of_birth = forms.DateField(label='DOB', widget=forms.TextInput(attrs={"class": "form-control date-picker"}))
	gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect())
	education = forms.ChoiceField(label='Education', choices=EDUCATION_CHOICES, widget=forms.Select(attrs={"class": "form-control"}))
	profile = forms.CharField(label='Profile', max_length=250, widget=forms.FileInput(attrs={"class": "form-control"}))

	def __init__(self, *args, **kwargs):
		super(Application, self).__init__(*args, **kwargs)
