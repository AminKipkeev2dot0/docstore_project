from django.forms import ModelForm
from .models import Doc

class DocForm(ModelForm):
    class Meta:
        model = Doc
        fields = ('title','descr','scan')