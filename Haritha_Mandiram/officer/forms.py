from django.forms import DateInput, ModelForm
from .models import Schem,Notification

class CreateSchemForm(ModelForm):
    class Meta:
        model=Schem
        fields='__all__'

class CreateNotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }