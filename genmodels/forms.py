from django.forms import ModelForm
from .models import MLModel

class MLModelForm(ModelForm):
    class Meta:
        model = MLModel
        fields = ["name", "description", "year"]
