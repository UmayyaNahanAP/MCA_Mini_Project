from django.forms import ModelForm
from officer.models import HM_User


class HMUserRegistrationForm(ModelForm):
    class Meta:
        model=HM_User
        fields='__all__'
