from rest_framework.viewsets import ModelViewSet

from .models import Settings
from .serializers import SettingsSerializer

class SettingsViewSet(ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
