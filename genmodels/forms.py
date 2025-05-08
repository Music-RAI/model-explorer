from django.forms import ModelForm
from moderation.forms import BaseModeratedObjectForm
from .models import MLModel

class MLModelForm(BaseModeratedObjectForm):
# class MLModelForm(ModelForm):
    class Meta:
        model = MLModel
        fields = [
            "identifier",
            "name",
            "description",
            "year",
            "website",
            "dataset",
            "license_type",
            "is_free",
            "is_open_source",
            "has_real_time_inference",
            "are_checkpoints_available",
            "can_finetune",
            "can_train_from_scratch",
            "interactions",
            "technology",
            "input_types",
            "output_types",
            "tags",
        ]
