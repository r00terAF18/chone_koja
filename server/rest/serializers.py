from rest_framework.serializers import ModelSerializer
from django.contrib.admin.models import LogEntry

from mini.models import Room


class LogSer(ModelSerializer):
    class Meta:
        model = LogEntry
        fields = "__all__"


class RoomSer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
