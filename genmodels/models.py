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

YES_NO_UNKNOWN = [
    ("Y", "Yes"),
    ("N", "No"),
    ("U", "Don't know"),
]

class MLModel(models.Model):
    class Meta:
        verbose_name = "ML Model"
        verbose_name_plural = "ML Models"

    id = models.CharField(max_length=20, unique=True, primary_key=True)
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

    technology = models.ManyToManyField(Technology)
    categories = models.ManyToManyField(Category)
    capabilities = models.ManyToManyField(Capability)
    input_types = models.ManyToManyField(InputType)
    output_types = models.ManyToManyField(OutputType)
    time_to_produce_output = models.ManyToManyField(TimeToProduceOutput)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
