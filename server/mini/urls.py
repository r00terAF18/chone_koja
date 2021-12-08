from django.urls import path, include

from mini.views import index

urlpatterns = [
    path("", index, name="index"),
]
