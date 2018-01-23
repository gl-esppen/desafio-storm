# -*- coding: utf-8 -*-

from django.contrib import admin
from src.models import Filme, Ator, Genero


class AtorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais')
    list_filter = ('pais',)

    search_fields = ['nome', 'pais']

    fieldsets = (
        ('Dados do Ator', {
            'fields': ('nome', 'pais', 'imagem'),
        }),
    )


class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ['nome']

    fieldsets = (
        ('Dados do Gênero', {
            'fields': ('nome',),
        }),
    )


class FilmeAdmin(admin.ModelAdmin):

    list_display = ('nome','display_image', 'get_atores', 'get_generos')
    list_filter = ('atores__nome', 'generos__nome')

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

    def display_image(self, obj):
        return '<img src="%s" width="200px"/>' % obj.imagem.url

    display_image.allow_tags = True

    def get_atores(self, obj):
        return "\n".join([a.nome for a in obj.atores.all()])

    def get_generos(self, obj):
        return "\n".join([g.nome for g in obj.generos.all()])


admin.site.register(Filme, FilmeAdmin)
admin.site.register(Ator, AtorAdmin)
admin.site.register(Genero, GeneroAdmin)
