from django.forms import ModelForm
from django.forms import EmailField, PasswordInput, CharField
from .models import Vayal_User
from officer.models import Complaint


class VayalUserRegistrationForm(ModelForm):
    email = EmailField()
    password = CharField(widget=PasswordInput())
    class Meta:
        model=Vayal_User
        fields=['name','dob','genter','phone_number']


class CreateComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description']

