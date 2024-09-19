from django.shortcuts import render
from rest_framework import viewsets
from apps.users.models import User
from .serializers import UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
