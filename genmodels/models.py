from django.db import models
from moderation import moderation

from .moderators import MLModelModerator

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class InputType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class OutputType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TimeToProduceOutput(models.Model):
    class Meta:
        verbose_name_plural = "times to produce output"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Capability(models.Model):
    class Meta:
        verbose_name_plural = "capabilities"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Technology(models.Model):
    class Meta:
        verbose_name_plural = "technologies"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

YES_NO_UNKNOWN = [
    ("Y", "Yes"),
    ("N", "No"),
    ("U", "Don't know"),
]

class MLModel(models.Model):
    class Meta:
        verbose_name = "ML Model"
        verbose_name_plural = "ML Models"

    identifier = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField(blank=True)
    website = models.URLField(blank=True)
    paper = models.CharField(max_length=500, blank=True)
    dataset = models.CharField(max_length=500, blank=True)
    output_length = models.CharField(max_length=100, blank=True)
    license_type = models.CharField(max_length=100, blank=True)
    is_free = models.CharField(max_length=1, choices=YES_NO_UNKNOWN, default="U")
    is_open_source = models.CharField(max_length=1, choices=YES_NO_UNKNOWN, default="U")
    has_real_time_inference = models.CharField(
        max_length=1,
        choices=YES_NO_UNKNOWN,
        default="U",
    )
    are_checkpoints_available = models.CharField(
        max_length=1,
        choices=YES_NO_UNKNOWN,
        default="U",
    )
    can_finetune = models.CharField(max_length=1, choices=YES_NO_UNKNOWN, default="U")
    can_train_from_scratch = models.CharField(
        max_length=1,
        choices=YES_NO_UNKNOWN,
        default="U",
    )
    low_resource = models.CharField(max_length=1, choices=YES_NO_UNKNOWN, default="U")
    interactions = models.CharField(max_length=500, blank=True)

    technology = models.ManyToManyField(Technology, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    capabilities = models.ManyToManyField(Capability, blank=True)
    input_types = models.ManyToManyField(InputType, blank=True)
    output_types = models.ManyToManyField(OutputType, blank=True)
    time_to_produce_output = models.ManyToManyField(TimeToProduceOutput, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

moderation.register(MLModel, MLModelModerator)
