from django.urls import path

from .views import *
from .views_Room import *

urlpatterns = [
    # path("all/", room_list),
    path("create/", room_create),
    path("detail/<int:id>/", room_detail),
    path("compare/add/<int:id>", add_to_compare),
    path("search/", search_room),
]
