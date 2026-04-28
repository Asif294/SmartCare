from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serialzers
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset=models.Appintment.objects.all()
    serializer_class=serialzers.AppintmentSerializer


    def get_queryset(self):
        queryset=super().get_queryset()
        print(self.request.query_params)
        patient_id=self.request.query_params.get('patient_id')
        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset