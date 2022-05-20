from django.urls import path
from . import views

urlpatterns = [
    # path("", hello, name="home"),
    path('', views.home, name='index'),
    path('escala', views.escala, name='escala'),
    path('recomendaciones', views.recomendaciones, name='recomendaciones'),
    path('blog', views.blog, name='blog'),
    path('enlaces', views.enlaces, name='enlaces'),
    path('fotos', views.fotos, name='fotos'),
]

