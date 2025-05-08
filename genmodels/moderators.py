from moderation.constants import MODERATION_STATUS_APPROVED
from moderation.managers import ModerationObjectsManager
from moderation.models import STATUS_CHOICES
from moderation.moderator import GenericModerator

class MultipleModerationObjectsManager(ModerationObjectsManager):
    def filter_moderated_objects(self, queryset):
        _, approved = STATUS_CHOICES[MODERATION_STATUS_APPROVED]
        return [q for q in queryset if q.moderated_status == approved]

class MLModelModerator(GenericModerator):
    keep_history = True
    moderation_manager_class = MultipleModerationObjectsManager
