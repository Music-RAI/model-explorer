from django.db.models import Count, Q
from moderation.constants import MODERATION_READY_STATE
from moderation.managers import ModerationObjectsManager
from moderation.moderator import GenericModerator

class MultipleModerationObjectsManager(ModerationObjectsManager):
    def filter_moderated_objects(self, queryset):
        annotated_queryset = queryset.annotate(
            num_moderation_objects=Count('_relation_object')
        )

        only_ready = {
            '_relation_object__state': MODERATION_READY_STATE,
        }

        return annotated_queryset.filter(Q(**only_ready))

class MLModelModerator(GenericModerator):
    keep_history = True
    moderation_manager_class = MultipleModerationObjectsManager
