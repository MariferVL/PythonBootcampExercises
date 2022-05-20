from pyexpat import features
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from  django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import *
from .forms import *


# Create your views here. 

def home(request):
    return render(request, 'bp/home.html', {'home': home})

def profile(request):
    return render(request, 'bp/profile.html', {'profile': profile})

def config(request):
    return render(request, 'bp/config.html', {'config': config})

def presents(request):
    presents = Presents.objects.all()
    return render(request, 'bp/presents.html', {'presents': presents})

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
    return render(request, "bp/contact.html", {'form': form})

def success(request):
    return render(request, 'bp/success.html', {'success': success})

def message_list(request):
    messages = Contact.objects.order_by('sending_date')
    return render(request, 'bp/message_list.html', {'messages': messages})

@login_required
def my_messages(request):
    email= request.user.email
    my_messages = Contact.objects.filter(sender= email).all().order_by('sending_date')
    return render(request, 'bp/my_messages.html', {'my_messages': my_messages})


def message_detail(request,pk):
    message = get_object_or_404(Contact, pk=pk)
    return render(request, 'bp/message_detail.html', {'message': message})

@login_required
def message_remove(request,pk):
    message = get_object_or_404(Contact, pk=pk)
    message.delete()
    return redirect('message_list')

def postIt(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'bp/post-it.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'bp/post_detail.html', {'post': post})

@login_required
def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else: 
        form = PostForm()
    return render(request, 'bp/post_edit.html',{'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'bp/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post-it')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'bp/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def abp(request):
    return render(request, 'bp/abp.html', {'abp': abp})

def usersInfo(request):
    users = User.objects.all()
    return render(request, 'bp/users_info.html', {'users': users})


