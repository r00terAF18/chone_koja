from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType

# from .models import *

# adds log entry for adding, editing and removing of any model
def add_log(model_name, object_id, object_repr, action):
    content_type = ContentType.objects.get_for_model(model_name)
    LogEntry.objects.log_action(
        user_id=1,
        content_type_id=content_type.pk,
        object_id=object_id,
        object_repr=object_repr,
        action_flag=action,
    )
