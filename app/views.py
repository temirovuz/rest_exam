from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import UserPasswordManager
from .serializers import UserPasswordManagerSerializer


class UserPasswordManagerViewSet(ModelViewSet):
    queryset = UserPasswordManager.objects.all()
    serializer_class = UserPasswordManagerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['application_type']
