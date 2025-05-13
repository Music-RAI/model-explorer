from django.forms import ModelForm
from moderation.forms import BaseModeratedObjectForm
from .models import MLModel

class MLModelForm(BaseModeratedObjectForm):
# class MLModelForm(ModelForm):
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
