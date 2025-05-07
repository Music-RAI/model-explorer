from django.contrib import admin
from moderation.admin import ModerationAdmin

from .models import (
    Capability,
    Category,
    InputType,
    MLModel,
    OutputType,
    Tag,
    Technology,
    TimeToProduceOutput,
)

admin.site.register(Capability)
admin.site.register(Category)
admin.site.register(InputType)
admin.site.register(OutputType)
admin.site.register(Tag)
admin.site.register(Technology)
admin.site.register(TimeToProduceOutput)

class MLModelAdmin(ModerationAdmin): pass
admin.site.register(MLModel, MLModelAdmin)
