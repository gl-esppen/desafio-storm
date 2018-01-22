from rest_framework import serializers
from src import models


class AtorSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Ator
		fields = '__all__'


class GeneroSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Genero
		fields = '__all__'


class FilmeSerializer(serializers.ModelSerializer):

	atores = AtorSerializer(many=True)
	generos = GeneroSerializer(many=True)

	class Meta:
		model = models.Filme
		fields = '__all__'