from django.forms import ModelForm
from django.forms import EmailField, PasswordInput, CharField
from .models import Vayal_User


class VayalUserRegistrationForm(ModelForm):
    email = EmailField()
    password = CharField(widget=PasswordInput())
    class Meta:
        model=Vayal_User
        fields=['name','dob','genter','phone_number']

