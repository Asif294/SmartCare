from django.shortcuts import render
from rest_framework import viewsets,pagination,filters
from .import models
from .import serialzers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class DoctorViewset(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all()
    serializer_class=serialzers.DoctorSerializer

class SpecializatioViewset(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all()
    serializer_class=serialzers.SpecializatioSerializer

class DoctorPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100


class DesignationViewset(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()
    serializer_class=serialzers.DesignationSerializer
    filter_backends=[filters.SearchFilter]
    pagination_class =DoctorPagination
    search_fields=['user_firstname','user_email','designation_name','specialization_name']

class AvailableTimeviewsSpecalistDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset 


class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=models.AvailableTime.objects.all()
    serializer_class=serialzers.AvailableTimeSerializer
    filter_backends =[AvailableTimeviewsSpecalistDoctor]

class ReviewViewset(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serialzers.ReviewSerializer



    def get_queryset(self):
        queryset=super().get_queryset()
        
        doctor_id=self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset=queryset.filter(doctor_id=doctor_id)
        return queryset