from django.contrib.auth.models import User

from rest_framework import viewsets

from users.models import Profile
from users.permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrReadOnly
from users.serializers import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrGetAndPostOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrReadOnly]
    http_method_names = ["get", "put", "patch"]
