from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .viewsets import SettingsViewSet


router = DefaultRouter()
router.register("settings", SettingsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
