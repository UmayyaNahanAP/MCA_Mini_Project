from django.forms import ModelForm,DateInput
from django.forms import EmailField, PasswordInput, CharField
from .models import Agricultural_officer,Vayal_User,Scheme,SchemeApplication,VegetablePermission,Vegetable,VegetablePurchase,Notification,Complaint,LeaseLand


class DateInput(forms.DateInput):
    input_type = 'date'

class Agricultural_officerRegistrationForm(ModelForm):
    email = EmailField()
    password = CharField(widget=PasswordInput())
    class Meta:
        model=Vayal_User
        fields=['name','phone_number',' unique_code']
        widgets = {'dob': DateInput()}


class VayalUserRegistrationForm(ModelForm):
    email = EmailField()
    password = CharField(widget=PasswordInput())
    class Meta:
        model=Vayal_User
        fields=['name','dob','gender','phone_number','aadhar_number','cast',
               'house_name','place','village','pincode','land_ownership','photo']
        widgets = {'dob': DateInput()}


class CreateSchemeForm(ModelForm):
    class Meta:
        model=Scheme
        fields=['name','type','description','criteria','cast_eligibility','land_ownership','start_date','end_date']
        widgets = {
            'end_date': DateInput()
        }


class SchemeApplicationForm(ModelForm):
    class Meta:
        model=SchemeApplication
        fields=['benefiting','house_number','ward_number','total_land_area','land_survay_no',
                'bank_name','branch','account_no','sign','aadhar','land_tax','bank_pass']


class VegetablePermissionForm(ModelForm):
    class Meta:
        model=VegetablePermission
        fields = ['farm_name','farm_place','total_land_area','land_survay_no','sign','aadhar','land_tax']

class VegetableForm(ModelForm):
    class Meta:
        model=Vegetable
        fields=['name','price','quantity','expiry','photo']
        widgets = {'posted_date': DateInput()}

from django import forms
class VegetablePurchaseForm(ModelForm):
    class Meta:
        model=VegetablePurchase
        fields=['quantity','total_price']
        widgets = {
            'purchase_date': DateInput(),
        }



class CreateComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['title','description']
        widgets = {'created_at': DateInput()}
        

class CreateNotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['title','description']
        widgets = {
            'date': DateInput()
        }

class LeaseLandForm(ModelForm):
    class Meta:
        model=LeaseLand
        fields=['land_name','location','period','land_lease_rent','photo']

        