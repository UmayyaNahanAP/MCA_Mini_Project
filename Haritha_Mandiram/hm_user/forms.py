from django.forms import ModelForm
from django.forms import EmailField, PasswordInput, CharField
from officer.models import HM_User,Complaint,VegitablePermissionForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
# class HMUserRegistrationForm(ModelForm):
#     # email = EmailField()
#     # password = CharField(widget=PasswordInput())
#     class Meta:
#         model=HM_User
#         fields = '__all__'
#         exclude = ['user']


class HMUserRegistrationForm(ModelForm):
    email = EmailField()
    password = CharField(widget=PasswordInput())
    class Meta:
        model=HM_User
        fields=['name','dob','genter','phone_number']


class CreateComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description']

class CreateVegitablePermissionForm(ModelForm):
    class Meta:
        model=VegitablePermissionForm
        fields='__all__'


