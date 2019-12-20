from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Language,Paradigm,Programmer
from .serializers import LanguageSerializers,ParadigmSerializers,ProgrammerSerializers
# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset=Language.objects.all()
    serializer_class=LanguageSerializers

class ParadigmView(viewsets.ModelViewSet):
    queryset=Paradigm.objects.all()
    serializer_class=ParadigmSerializers

class ProgrammerView(viewsets.ModelViewSet):
    queryset=Programmer.objects.all()
    serializer_class=ProgrammerSerializers
