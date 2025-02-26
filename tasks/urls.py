from django.urls import include, path
from rest_framework import routers

from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("", include(router.urls)),
]