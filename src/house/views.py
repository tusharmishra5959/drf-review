from rest_framework import viewsets

from house.models import House
from house.permissions import IsHouseManagerOrNone
from house.serializers import HouseSerializer


class HouseViewSet(viewsets.ModelViewSet):
    """."""

    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsHouseManagerOrNone]
