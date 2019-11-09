from rest_framework import viewsets
from .serializers import SiteSerializer,ConfigurationSerializer,ModerationSerializer
from .models import Site,Configuration,ModerationSetting


class SiteView(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class ConfigurationView(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer


class ModerationView(viewsets.ModelViewSet):
    queryset = ModerationSetting.objects.all()
    serializer_class = ModerationSerializer
