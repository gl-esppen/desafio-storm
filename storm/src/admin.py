from django.contrib import admin
from src.models import Filme, Ator, Genero


class AtorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ator, AtorAdmin)



class GeneroAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genero, GeneroAdmin)



class FilmeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Filme, FilmeAdmin)