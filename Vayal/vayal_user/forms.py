from django.forms import ModelForm
from django.forms import EmailField, PasswordInput, CharField
from .models import Vayal_User


class VayalUserRegistrationForm(ModelForm):
    email = EmailField()
    password = CharField(widget=PasswordInput())
    class Meta:
        model=Vayal_User
        fields=['name','dob','gender','phone_number','aadhar_number','cast',
               'house_name','place','village','pincode','land_ownership']
            #    ,'photo']
