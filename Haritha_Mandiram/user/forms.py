from django.forms import ModelForm
from officer.models import SchemApplication

class SchemApplicationForm(ModelForm):
    class Meta:
        model=SchemApplication
        fields='__all__'