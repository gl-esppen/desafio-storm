# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView
from src.models import Ator, Genero, Filme

class FilmeListView(ListView):
	model = Filme
	context_object_name = 'filmes'
	template_name = 'filmes.html'

	def get_queryset(self):
		queryset = Filme.objects.all()

		#filtro por genero
		if 'genero' in self.request.GET:
			genero = self.request.GET.get('genero')
			queryset = queryset.filter(generos=genero)

		#ordenacao
		if 'ordem' in self.request.GET:
			flow = self.request.GET.get('ordem')
			order = 'nome' if flow == 'DESC' else '-nome'
			queryset = queryset.order_by(order)

		return queryset


class FilmeDetailView(DetailView):
	model = Filme
	context_object_name = 'filme'
	template_name = 'filme.html'


class AtorDetailView(DetailView):
	model = Ator
	context_object_name = 'ator'
	template_name = 'ator.html'