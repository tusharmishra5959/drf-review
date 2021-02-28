from django.utils import timezone
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as s

from task.models import TaskList, Task, Attachment, NOT_COMPLETE, COMPLETE
from task.permissions import IsAllowedToEditTaskListElseNone, IsAllowedToEditTaskElseNone, \
    IsAllowedToEditAttachmentElseNone
from task.serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer


class TaskListViewSet(viewsets.ModelViewSet):
    """."""

    queryset = TaskList.objects.all()
    permission_classes = [IsAllowedToEditTaskListElseNone]
    serializer_class = TaskListSerializer
    # http_method_names = []

    def list(self, request, *args, **kwargs):
        """."""

        return Response({"detail": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TaskViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAllowedToEditTaskElseNone]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'status', ]
    filterset_fields = ['status', ]

    def get_queryset(self):
        """."""

        queryset = super(TaskViewSet, self).get_queryset()
        user_profile = self.request.user.profile
        updated_queryset = queryset.filter(created_by=user_profile)
        return updated_queryset

    @action(detail=True, methods=["patch"])
    def update_task_status(self, request, pk=None):
        """."""

        try:
            task = self.get_object()
            profile = request.user.profile
            status = request.data['status']

            if status == NOT_COMPLETE:
                if task.status == COMPLETE:
                    task.status = NOT_COMPLETE
                    task.completed_at = None
                    task.completed_by = None
                else:
                    raise Exception("Task is already marked as not complete")
            elif status == COMPLETE:
                if task.status == NOT_COMPLETE:
                    task.status = COMPLETE
                    task.completed_at = timezone.now()
                    task.completed_by = profile
                else:
                    raise Exception("Task is already marked as complete")
            else:
                raise Exception("Incorrect status provided")
            task.save()
            serializer = TaskSerializer(instance=task, context={"request": request})
            return Response(serializer.data, status=s.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=s.HTTP_400_BAD_REQUEST)


class AttachmentViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [IsAllowedToEditAttachmentElseNone]

    def list(self, request, *args, **kwargs):
        """."""

        return Response({"detail": "Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

