from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('log_out', views.logout_user, name='logout'),

    path('register_user', views.register_user, name='register_user'), #register_user

    # path('users/', include('django.contrib.auth.urls')),
    # path('users/', include('users.urls')),
]