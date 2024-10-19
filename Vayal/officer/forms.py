from django.forms import ModelForm,DateInput
from .models import Notification



class CreateNotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }