from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from django.utils.timezone import localdate
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get("status", None)
        today = localdate()

        if status:
            status = status.lower()
            if status == "incoming":
                return queryset.filter(due_date__gt=today)
            elif status == "today":
                return queryset.filter(due_date=today)
            elif status == "overdue":
                return queryset.filter(due_date__lt=today)
            else:
                raise ValidationError(
                    {"status": "Invalid value for status. Accepted values are 'incoming', 'today', or 'overdue'."}
                )

        return queryset