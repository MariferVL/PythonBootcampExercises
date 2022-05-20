from django.shortcuts import render,redirect
from web.models import Funfact,Scale,Tip,Post,Link,Photo

from random import randint




# -------------------------------------------------------
# from django import forms
from django.core.mail import send_mail#, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.utils import timezone
from .models import *
from .forms import *


# Create your views here.

# from django.http import HttpResponse
# def hello(request):
#   return HttpResponse("Hello, World! i'm <b>appoo project</b>")

def admin(request):
  return redirect('admin/')



def home(request):
  # query_funfacts = Funfact.objects.all()
  len_obj = len(Funfact.objects.all())
  query_funfacts = Funfact.objects.all()[randint(0, len_obj-1)]
  # value = randint(0, 10)
  return render(request,'web/home.html',{'nbar':'home','query_funfacts':query_funfacts})
  


def escala(request):
  query_scale = Scale.objects.all()
  return render(request,'web/escala.html',{'nbar':'escala','query_scale':query_scale})

def recomendaciones(request):
  query_tips = Tip.objects.all()
  return render(request,'web/recomendaciones.html',{'nbar':'recomendaciones','query_tips':query_tips})

def blog(request):
  query_posts = Post.objects.all()
  return render(request,'web/blog.html',{'nbar':'blog','query_posts':query_posts})

def enlaces(request):
  query_links = Link.objects.all()
  return render(request,'web/enlaces.html',{'nbar':'enlaces','query_links':query_links})

def fotos(request):
  len_obj = len(Photo.objects.all())
  query_photos = Photo.objects.all()[randint(0, len_obj-1)]
  return render(request,'web/fotos.html',{'nbar':'fotos','query_photos':query_photos})








# ---------------------------------------------

def contact(request):
  if request.method == 'GET':
    form = ContactForm()
  else:
    form = ContactForm(request.POST)
    if form.is_valid():
      contact = form.save()
      name = form.cleaned_data['name']
      sender = form.cleaned_data['sender']
      subject = form.cleaned_data['subject']
      message = form.cleaned_data['message']
      cc_myself = form.cleaned_data['cc_myself']
      contact.sending_date = timezone.now()
      contact.save()

      recipients = []
      if cc_myself:
        recipients.append(sender)

      send_mail(subject, message,"", recipients)
      # The signature for the send_email method is:
      # send_mail(subject, message, from_email, recipient_list, fail_silently=False, 
      # auth_user=None, auth_password=None, connection=None, html_message=None)
      return redirect('success')
  return render(request, "web/contact.html", {'nbar':'contacto','form': form})

def success(request):
  return render(request, 'web/success.html', {'success': success})


def message_list(request):
  messages = Contact.objects.order_by('sending_date')
  return render(request, 'web/message_list.html', {'messages': messages})


@login_required
def my_messages(request):
  email = request.user.email
  my_messages = Contact.objects.filter(sender=email).all().order_by('sending_date')
  return render(request, 'web/my_messages.html', {'my_messages': my_messages})


def message_detail(request,pk):
  message = get_object_or_404(Contact, pk=pk)
  return render(request, 'web/message_detail.html', {'message': message})


@login_required
def message_remove(request,pk):
  message = get_object_or_404(Contact, pk=pk)
  message.delete()
  return redirect('message_list')