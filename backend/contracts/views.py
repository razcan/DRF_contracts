from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import (
    ContractSerializer
)
from .models import Contract

class ContractViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticated,)  

    ordering_fields = ['id']
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    pagination_class = PageNumberPagination
