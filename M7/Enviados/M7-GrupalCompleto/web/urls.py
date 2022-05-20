from django.urls import path
from . import views


urlpatterns = [
  # path("", hello, name="home"),
  path('admin/', views.admin, name='admin'),
  
  path('', views.home, name='home'),
  path('escala', views.escala, name='escala'),
  path('recomendaciones', views.recomendaciones, name='recomendaciones'),
  path('blog', views.blog, name='blog'),
  path('enlaces', views.enlaces, name='enlaces'),
  path('fotos', views.fotos, name='fotos'),
  # --------------------------------------------
  path('contact', views.contact, name='contact'),
  path('messages', views.message_list, name='message_list'),
  path('mymessages', views.my_messages, name='my_messages'),
  path('messages/<int:pk>/',views.message_detail, name='message_detail'),
  path('messages/<pk>/remove', views.message_remove, name='message_remove'),
  path('sent',views.success, name='success'),
]






