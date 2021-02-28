from rest_framework import routers

from house.views import HouseViewSet

router = routers.DefaultRouter()
router.register("houses", HouseViewSet)

urlpatterns = router.urls