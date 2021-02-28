from rest_framework import routers
from .views import UserViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns = router.urls
