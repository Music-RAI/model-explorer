from moderation.moderator import GenericModerator
from moderation.managers import ModerationObjectsManager

class MultipleModerationObjectsManager(ModerationObjectsManager):
    def filter_moderated_objects(self, queryset):
        return queryset

class MLModelModerator(GenericModerator):
    keep_history = True
    moderation_manager_class = MultipleModerationObjectsManager
