from django.forms import ModelForm,DateInput
from .models import Scheme,SchemeApplication,Notification,Complaint



class CreateSchemeForm(ModelForm):
    class Meta:
        model=Scheme
        fields='__all__'

class SchemeApplicationForm(ModelForm):
    class Meta:
        model=SchemeApplication
        fields='__all__'


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
        