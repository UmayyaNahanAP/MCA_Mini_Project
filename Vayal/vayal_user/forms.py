from django.forms import ModelForm
from django.forms import EmailField, PasswordInput, CharField
from .models import Vayal_User,LeaseLand
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class VayalUserRegistrationForm(ModelForm):
    email = EmailField()
    password = CharField(widget=PasswordInput())
    class Meta:
        model=Vayal_User
        fields=['name','dob','gender','phone_number','aadhar_number','cast',
               'house_name','place','village','pincode','land_ownership','photo']
        widgets = {'dob': DateInput()}


class LeaseLandForm(ModelForm):
    class Meta:
        model=LeaseLand
        fields=['land_name','location','period','land_lease_rent','photo']