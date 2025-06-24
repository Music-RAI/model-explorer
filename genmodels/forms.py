from captcha.fields import CaptchaField
from django import forms
from moderation.forms import BaseModeratedObjectForm

from .models import MLModel

class MLModelForm(BaseModeratedObjectForm):
    captcha = CaptchaField()

    class Meta:
        model = MLModel
        fields = [
            "name",
            "description",
            "year",
            "website",
            "input_types",
            "output_types",
            "output_length",
            "technology",
            "dataset",
            "license_type",
            "has_real_time_inference",
            "is_free",
            "is_open_source",
            "are_checkpoints_available",
            "can_finetune",
            "can_train_from_scratch",
            "tags",
        ]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    title = forms.CharField(max_length=200, required=True, label='Message title')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
    captcha = CaptchaField()
