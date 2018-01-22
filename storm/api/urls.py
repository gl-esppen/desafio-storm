from . import views
from rest_framework import routers


router = routers.SimpleRouter()

router.register(r'filmes', views.FilmeViewSet)
router.register(r'ator', views.AtorViewSet)
router.register(r'genero', views.GeneroViewSet)

urlpatterns = router.urls