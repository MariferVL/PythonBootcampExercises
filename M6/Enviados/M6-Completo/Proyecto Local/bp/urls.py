from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name= 'home'),
    path('profile',views.profile, name='profile'),
    path('settings',views.config, name='config'),
    path('presents',views.presents, name='presents'),
    path('contact', views.contact, name='contact'),
    path('messages', views.message_list, name='message_list'),
    path('mymessages', views.my_messages, name='my_messages'),
    path('messages/<int:pk>/',views.message_detail, name='message_detail'),
    path('messages/<pk>/remove', views.message_remove, name='message_remove'),
    path('sent',views.success, name='success'),
    path('post',views.postIt, name='post-it'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('abp',views.abp, name='abp'),
    path('abp/usersInfo', views.usersInfo, name='usersInfo'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

