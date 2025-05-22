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
    ("U", "Not known"),
]

FREE_YES_NO = [
    ("Y", "Yes"),
    ("N", "No"),
    ("B", "Yes and No, depending on the plan"),
    ("U", "Not known"),
]

class MLModel(models.Model):
    class Meta:
        verbose_name = "ML Model"
        verbose_name_plural = "ML Models"

    identifier = models.CharField(max_length=20, unique=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True)
    input_types = models.ManyToManyField(InputType, blank=True)
    output_types = models.ManyToManyField(OutputType, blank=True)
    output_length = models.CharField(max_length=100, blank=True)
    technology = models.ManyToManyField(Technology, blank=True)
    dataset = models.CharField(max_length=500, blank=True)
    license_type = models.CharField(max_length=100, blank=True)
    has_real_time_inference = models.CharField(
        max_length=1,
        choices=YES_NO_UNKNOWN,
        default="U",
    )
    is_free = models.CharField(max_length=1, choices=FREE_YES_NO, default="U")
    is_open_source = models.CharField(max_length=1, choices=YES_NO_UNKNOWN, default="U")
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
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    def _name_to_identifier(self):
        """
        Convert a name to an identifier by removing whitespace and replacing spaces with hyphens.
        """
        name = self.name.lower()
        identifier = name.replace(' ', '-').strip('-')
        return identifier

    def save(self, *args, **kwargs):
        def name_changed():
            if self.pk is not None:
                orig = MLModel.objects.get(pk=self.pk)
                if orig.name == self.name:
                    return False
            return True

        if name_changed() or not self.identifier:
            self.identifier = self._name_to_identifier()
        super().save(*args, **kwargs)

moderation.register(MLModel, MLModelModerator)
