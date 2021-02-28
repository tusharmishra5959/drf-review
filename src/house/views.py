from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from house.models import House
from house.permissions import IsHouseManagerOrNone
from house.serializers import HouseSerializer


class HouseViewSet(viewsets.ModelViewSet):
    """."""

    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsHouseManagerOrNone]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['points', 'completed_tasks_count', 'not_completed_tasks_count']
    search_fields = ['=name', 'description']
    filterset_fields = ['members', ]

    @action(detail=True, methods=['post'], name='Join', permission_classes=[])
    def join(self, request, pk=None):
        """."""

        try:
            house = self.get_object()
            user_profile = request.user.profile
            if user_profile.house is None:
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif user_profile in house.members.all():
                return Response({"detail": "Already a member in this house."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"detail": "Already a member of another house."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'], name='Leave', permission_classes=[])
    def leave(self, request, pk=None):
        """."""

        try:
            house = self.get_object()
            user_profile = request.user.profile
            if user_profile in house.members.all():
                user_profile.house = None
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"detail": "User is not a member of this house."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=["post"], name="Remove Member")
    def remove_member(self, request, pk=None):
        """."""

        try:
            house = self.get_object()
            user_id = request.data.get("user_id", None)
            if user_id is None:
                return Response({"user_id": "Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
            user_profile = User.objects.get(pk=user_id).profile
            house_members = house.members
            if user_profile in house_members.all():
                house_members.remove(user_profile)
                house.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"detail": "Use not a member of the house"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as e:
            return Response({"detail": "User_id doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
