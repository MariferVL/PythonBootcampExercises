from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name= 'home'),
    path('profile',views.profile, name='profile'),
    path('settings',views.config, name='config'),
    path('post',views.postIt, name='post-it'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('abp',views.abp, name='abp'),
    path('abp/usersInfo', views.usersInfo, name='usersInfo'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

