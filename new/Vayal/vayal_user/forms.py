from django.forms import ModelForm
from django.forms import EmailField, PasswordInput, CharField
from .models import Vayal_User
from officer.models import Complaint


class VayalUserRegistrationForm(ModelForm):
    email = EmailField()
    password = CharField(widget=PasswordInput())
    class Meta:
        model=Vayal_User
        fields=['name','dob','gender','phone_number','aadhar_number','cast',
                'house_name','place','village','pincode','land_ownership','photo']

    
    # class Meta:
    #     model=Vayal_User
    #     fields=['name','dob','genter','phone_number','aadhar_number','cast',
    #             'house_name','place','village','panchayat_muncipality_corporation',
    #             'district','pincode','house_number','ward_number','land_ownership',
    #             'total_land_area','land_survay_number','photo']



class CreateComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description']

