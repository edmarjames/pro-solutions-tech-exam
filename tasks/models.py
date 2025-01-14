from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.due_date} - {self.created_at}"

