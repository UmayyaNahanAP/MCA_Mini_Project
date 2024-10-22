from django.forms import ModelForm,DateInput
from .models import Scheme,SchemeApplication,VegetablePermission,Vegetable,Notification,Complaint



class CreateSchemeForm(ModelForm):
    class Meta:
        model=Scheme
        fields='__all__'

class SchemeApplicationForm(ModelForm):
    class Meta:
        model=SchemeApplication
        fields=['benefiting','house_number','ward_number','total_land_area','land_survay_no',
                'bank_name','branch','account_no','sign','aadhar','land_tax',]


class VegetablePermissionForm(ModelForm):
    class Meta:
        model=VegetablePermission
        fields = ['farm_name','farm_place']



class VegetableForm(ModelForm):
    class Meta:
        model=Vegetable
        fields=['name','price','quantity','expiry','photo']
       


class CreateComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['title','description']


class CreateNotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['title','description','date','published']
        widgets = {
            'date': DateInput()
        }
        