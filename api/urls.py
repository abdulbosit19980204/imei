from django.urls import path, include
from api.views import CustomUserViewSet, ArizaViewSet
from rest_framework import routers

urlpatterns = [
]
router = routers.SimpleRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('ariza', ArizaViewSet, basename='ariza')
urlpatterns += router.urls
