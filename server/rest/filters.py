from django_filters import rest_framework as filters
from mini.models import Room

class RoomFilter(filters.FilterSet):
    city = filters.CharFilter(lookup_expr='icontains')

    # rating__gt = django_filters.NumberFilter(field_name='rating', lookup_expr='gt')
    # rating__lt = django_filters.NumberFilter(field_name='rating', lookup_expr='lt')

    class Meta:
        model = Room
        fields = "__all__"