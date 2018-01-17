# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Ator(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    pais = models.CharField(max_length=150, verbose_name='País')

    class Meta:
        verbose_name = "Ator"
        verbose_name_plural = "Atores"
    
    def __unicode__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

    def __unicode__(self):
        return self.nome


class Filme(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    sinopse = models.TextField(verbose_name='Sinopse')
    imagem = models.ImageField(upload_to='filmes/imagens/', verbose_name='Imagem')
    atores = models.ManyToManyField(Ator, verbose_name='Atores')
    generos = models.ManyToManyField(Genero, verbose_name='Generos')

    def get_atores(self):
        return "\n".join([a.nome for a in self.atores.all()])
    get_atores.short_description = 'Atores'

    def get_generos(self):
        return "\n".join([g.nome for g in self.generos.all()])
    get_generos.short_description = 'Gêneros'

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"

    def __unicode__(self):
        return self.nome