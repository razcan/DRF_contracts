from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from .views import (
    ContractViewSet    
)
router = routers.DefaultRouter(trailing_slash=False)
router.register('contracts', ContractViewSet, basename='contracts')


urlpatterns = router.urls

urlpatterns += [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('contracts', ContractViewSet),    
]