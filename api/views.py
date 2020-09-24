from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, ProfileSerializer
from .models import Category, Profile

# Category views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('created_at')
    serializer_class = CategorySerializer

# Profile views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['hour', 'rating']
    filter_fields = ['category']
    ordering_fields = ['hour', 'rating']