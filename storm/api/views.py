from django.shortcuts import render
from rest_framework import viewsets

from src import models
from . import serializers

class FilmeViewSet(viewsets.ModelViewSet):
	queryset = models.Filme.objects.all()
	serializer_class = serializers.FilmeSerializer



class AtorViewSet(viewsets.ModelViewSet):
	queryset = models.Ator.objects.all()
	serializer_class = serializers.AtorSerializer


class GeneroViewSet(viewsets.ModelViewSet):
	queryset = models.Genero.objects.all()
	serializer_class = serializers.GeneroSerializer




