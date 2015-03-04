from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from .models import MicroService

# Serializers define the API representation.
class MicroServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroService
        
# ViewSets define the view behavior.
class MicroServiceViewSet(viewsets.ModelViewSet):
    queryset = MicroService.objects.all()
    serializer_class = MicroServiceSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'microservices', MicroServiceViewSet)
