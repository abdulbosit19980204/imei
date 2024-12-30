from django.urls import path, include
from api.views import CustomUserViewSet
from rest_framework import routers

urlpatterns = [
]
router = routers.SimpleRouter()
router.register('users', CustomUserViewSet, basename='users')
urlpatterns += router.urls
