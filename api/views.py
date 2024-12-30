from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.serializers import CustomUserSerializer, ArizaModelSerializer, JinoyatIshiSerializer
from api.permissions import IsSuperUser, IsOwnerOrReadOnly, IsJtonOwner
from api.models import CustomUser, ArizaModel, JinoyatIshiModel


class CustomUserViewSet(ModelViewSet):
    permission_classes = [IsJtonOwner | IsSuperUser, ]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class ArizaViewSet(ModelViewSet):
    permission_classes = [IsSuperUser | IsAuthenticated, IsOwnerOrReadOnly, ]
    queryset = ArizaModel.objects.all()
    serializer_class = ArizaModelSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(author=self.request.user, is_deleted=False)


class JinoyatIshiViewSet(ModelViewSet):
    permission_classes = [IsSuperUser | IsOwnerOrReadOnly, IsAuthenticated, ]
    queryset = JinoyatIshiModel.objects.all()
    serializer_class = JinoyatIshiSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(author=self.request.user, is_deleted=False)
