# -*- coding: utf-8 -*-

from django.contrib import admin
from src.models import Filme, Ator, Genero


class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais')
    list_filter = ('pais',)

    search_fields = ['nome', 'pais']

    fieldsets = (
        ('Dados do Ator', {
            'fields': ('nome', 'pais'),
        }),
    )


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    list_filter = ('nome',)

    search_fields = ['nome']

    fieldsets = (
        ('Dados do Gênero', {
            'fields': ('nome',),
        }),
    )


class FilmeAdmin(admin.ModelAdmin):

    list_display = ('nome','imagem', 'get_atores', 'get_generos')
    list_filter = ('nome',)

    search_fields = ['nome', 'atores__nome', 'generos__nome']

    fieldsets = (
        ('Dados do Filme', {
            'fields': ('nome','sinopse', 'imagem'),
        }),
        ('Atores', {
            'fields': ('atores',),
        }),
        ('Gêneros', {
            'fields': ('generos',),
        }),
    )


admin.site.register(Filme, FilmeAdmin)
admin.site.register(Ator, AtorAdmin)
admin.site.register(Genero, GeneroAdmin)
