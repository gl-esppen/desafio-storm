from django.conf.urls import url
from django.conf.urls import include
from . import views


urlpatterns = [
	url(r'^$', views.FilmeListView.as_view(), name='filmes'),
	url(r'^filme/(?P<pk>\d+)/$', views.FilmeDetailView.as_view(), name='filme'),
	url(r'^ator/(?P<pk>\d+)/$', views.AtorDetailView.as_view(), name='ator'),
]