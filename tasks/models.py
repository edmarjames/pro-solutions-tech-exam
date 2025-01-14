from django.db import models
from datetime import date


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def completed(self):
        today = date.today()
        if self.due_date > today:
            return "Incoming"
        elif self.due_date == today:
            return "Today"
        else:
            return "Overdue"

    def __str__(self):
        return f"{self.title} - {self.due_date} - {self.created_at}"

