from django.forms import ModelForm
from .models import commerce

class CommerceForm(ModelForm):
    class Meta:
        model=commerce
        fields='__all__'