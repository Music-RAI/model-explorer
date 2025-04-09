import uuid

from django.db import models

class Choice(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tag(Choice): pass
class InputType(Choice): pass
class OutputType(Choice): pass
class TimeToProduceOutput(Choice):
    class Meta:
        verbose_name_plural = "times to produce output"

class Category(Choice):
    class Meta:
        verbose_name_plural = "categories"

class Capability(Choice):
    class Meta:
        verbose_name_plural = "capabilities"

class Technology(Choice):
    class Meta:
        verbose_name_plural = "technologies"

class MLModel(models.Model):
    class Meta:
        verbose_name = "ML Model"
        verbose_name_plural = "ML Models"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField()
    website = models.URLField()
    paper = models.CharField(max_length=500)
    dataset = models.CharField(max_length=500)
    output_length = models.CharField(max_length=100)
    license_type = models.CharField(max_length=100)
    is_free = models.BooleanField()
    is_open_source = models.BooleanField()
    has_real_time_inference = models.BooleanField()
    are_checkpoints_available = models.BooleanField()
    can_finetune = models.BooleanField()
    can_train_from_scratch = models.BooleanField()
    low_resource = models.BooleanField()
    interactions = models.CharField(max_length=500)

    technology = models.ManyToManyField(Technology)
    categories = models.ManyToManyField(Category)
    capabilities = models.ManyToManyField(Capability)
    input_types = models.ManyToManyField(InputType)
    output_types = models.ManyToManyField(OutputType)
    time_to_produce_output = models.ManyToManyField(TimeToProduceOutput)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
