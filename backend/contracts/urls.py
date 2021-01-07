from django.urls import path
from rest_framework import routers
from .views import (
    ContractViewSet    
)
router = routers.DefaultRouter(trailing_slash=False)
router.register('contracts', ContractViewSet, basename='contracts')


urlpatterns = router.urls

urlpatterns += [
    path('contracts', ContractViewSet),
    
]