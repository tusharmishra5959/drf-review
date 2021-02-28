from rest_framework import routers

from task.views import TaskListViewSet, TaskViewSet, AttachmentViewSet

router = routers.DefaultRouter()
router.register("tasklists", TaskListViewSet)
router.register("tasks", TaskViewSet)
router.register("attachments", AttachmentViewSet)

urlpatterns = router.urls
