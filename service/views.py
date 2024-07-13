from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serialzers

class ServiceUsViewset(viewsets.ModelViewSet):
    queryset=models.Service.objects.all()
    serializer_class=serialzers.ServiceSerializer