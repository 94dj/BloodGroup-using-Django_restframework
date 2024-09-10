from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Patient
from api.serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
