from django.forms import ModelForm,DateInput
from .models import Scheme,Notification

class CreateSchemeForm(ModelForm):
    class Meta:
        model=Scheme
        fields='__all__'


class CreateNotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }