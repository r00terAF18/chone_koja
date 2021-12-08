from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import api_view

from .serializers import *
from .filters import *
from mini.models import Room

from .logger import add_log

search_list = []
compare_list = []


@api_view(["POST"])
def room_create(request):
    serializer = RoomSer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # room = Room.objects.latest("id")
        # object_id = room.id
        # object_repr = room.title
        # add_log(Room, object_id, object_repr, 1)
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors)


# @api_view(["GET"])
# def room_list(request):
#     rooms = Room.objects.all()
#     serializer = RoomSer(rooms, many=True)

#     return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def room_detail(request, id):
    try:
        room = Room.objects.get(id=id)
        object_id = room.id
        object_repr = room.title
    except Room.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == "GET":
        room_data = RoomSer(room)

        data = {"room": room_data.data}

        return Response(data)

    elif request.method == "PUT":
        serializer = RoomSer(instance=room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            add_log(Room, object_id, object_repr, 2)
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        room.delete()
        add_log(Room, object_id, object_repr, 3)
        return Response(status=HTTP_200_OK)


@api_view(["GET"])
def search_room(request):
    if request.method == "GET":
        rooms = RoomFilter(request.GET, queryset=Room.objects.all())
        serializer = RoomSer(rooms.qs, many=True)

        return Response(serializer.data)


@api_view(["GET"])
def add_to_compare(request, id):
    if request.method == "GET":
        room = Room.objects.get(id=id)
        return Response({"room": room})
