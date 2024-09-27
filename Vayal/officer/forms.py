from django.forms import ModelForm
from .models import Schem

class CreateSchemForm(ModelForm):
    class Meta:
        model=Schem
        fields='__all__'
