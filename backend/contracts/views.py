from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .serializers import (
    ContractSerializer
)
from .models import Contract

class ContractViewSet(viewsets.ModelViewSet):
    ordering_fields = ['id']
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    pagination_class = PageNumberPagination
