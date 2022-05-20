from django.shortcuts import render,redirect
from web.models import Funfact,Scale,Tip,Post,Link,Photo

from random import randint


# Create your views here.

# from django.http import HttpResponse
# def hello(request):
#   return HttpResponse("Hello, World! i'm <b>appoo project</b>")


def home(request):
  # query_funfacts = Funfact.objects.all()
  len_obj = len(Funfact.objects.all())
  query_funfacts = Funfact.objects.all()[randint(0, len_obj-1)]
  # value = randint(0, 10)
  return render(request,'web/home.html',{'query_funfacts':query_funfacts})
  


def escala(request):
  query_scale = Scale.objects.all()
  return render(request,'web/escala.html',{'query_scale':query_scale})

def recomendaciones(request):
  query_tips = Tip.objects.all()
  return render(request,'web/recomendaciones.html',{'query_tips':query_tips})

def blog(request):
  query_posts = Post.objects.all()
  return render(request,'web/blog.html',{'query_posts':query_posts})

def enlaces(request):
  query_links = Link.objects.all()
  return render(request,'web/enlaces.html',{'query_links':query_links})

def fotos(request):
  len_obj = len(Photo.objects.all())
  query_photos = Photo.objects.all()[randint(0, len_obj-1)]
  return render(request,'web/fotos.html',{'query_photos':query_photos})