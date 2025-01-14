from rest_framework.viewsets import ModelViewSet
from django.utils.timezone import localdate
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get("status", None)
        status = status.lower() if status else None
        today = localdate()

        if status == "incoming":
            return queryset.filter(due_date__gt=today)
        elif status == "today":
            return queryset.filter(due_date=today)
        elif status == "overdue":
            return queryset.filter(due_date__lt=today)
        return queryset