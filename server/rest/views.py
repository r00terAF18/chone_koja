from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *

from django.contrib.admin.models import LogEntry


@api_view(["GET"])
def home_page(request):
    l = LogEntry.objects.all()
    logs = LogSer(l, many=True)
    data = {"logs": logs.data}
    return Response(data)


@api_view(["POST"])
def add_room(request):
    print(request.data)
