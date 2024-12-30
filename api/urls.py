from api.views import CustomUserViewSet, ArizaViewSet, JinoyatIshiViewSet
from rest_framework import routers

urlpatterns = [
]
router = routers.SimpleRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('ariza', ArizaViewSet, basename='ariza')
router.register('jinoyatishi', JinoyatIshiViewSet, basename='jinoyatishi')
urlpatterns += router.urls
