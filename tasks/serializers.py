from rest_framework import serializers
from django.utils.timezone import localdate
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "due_date",
            "created_at",
            "completed"
        ]

    def get_completed(self, obj):
        today = localdate()
        if obj.due_date > today:
            return "Incoming"
        elif obj.due_date == today:
            return "Today"
        else:
            return "Overdue"