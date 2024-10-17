from django.forms import ModelForm,DateInput
from .models import Scheme,Notification,VegetablePermission
from django import forms


class VegetablePermissionForm(ModelForm):
    vegetable_names = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter vegetable names separated by commas'}),
        help_text="Separate each vegetable name with a comma (e.g., 'Tomato, Spinach, Carrot')"
    )

    class Meta:
        model = VegetablePermission
        fields = ['vayal_user', 'vegetable_names', 'farm_name', 'farm_address']

    def clean_vegetable_names(self):
        # Split the input by commas and trim whitespace
        data = self.cleaned_data['vegetable_names']
        return [item.strip() for item in data.split(',') if item.strip()]


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