from api.views import CustomUserViewSet, ArizaViewSet, JinoyatIshiViewSet, ProfileViewSet
from rest_framework import routers

urlpatterns = [
]
router = routers.SimpleRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('profile', ProfileViewSet, basename='profile')
router.register('ariza', ArizaViewSet, basename='ariza')
router.register('jinoyatishi', JinoyatIshiViewSet, basename='jinoyatishi')
urlpatterns += router.urls
