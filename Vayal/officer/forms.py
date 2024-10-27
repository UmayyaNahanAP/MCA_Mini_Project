from django.forms import ModelForm,DateInput
from .models import Scheme,SchemeApplication,VegetablePermission,Vegetable,Notification,Complaint



class CreateSchemeForm(ModelForm):
    class Meta:
        model=Scheme
        fields=['name','type','description','criteria','cast_eligibility','land_ownership','end_date']
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
        