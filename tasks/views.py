from rest_framework.viewsets import ModelViewSet
from django.utils.timezone import localdate
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer