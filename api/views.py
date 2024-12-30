from api.models import CustomUser, Device
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.serializers import CustomUserSerializer
from api.permissions import IsSuperUser, IsOwnerOrReadOnly, IsJtonOwner


class CustomUserViewSet(ModelViewSet):
    permission_classes = [IsJtonOwner | IsSuperUser, ]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
