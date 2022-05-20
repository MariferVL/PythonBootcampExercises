# login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 


# register
from django.contrib.auth.forms import UserCreationForm
from members.forms import RegisterUserForm
from .forms import RegisterUserForm
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'There Was An Error Login In, Try Again...')
            return redirect('../')
            
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You Were Logged Out!')
    return redirect('../')
    



def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            # messages.success(request, f'Account Created for {username}!')
            return redirect('../')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })
    
    # return render(request, 'authenticate/register_user.html', {'form': form})     
