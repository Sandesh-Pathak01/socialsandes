from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from profilesettings import models

# Create your views here.

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        logged_in = authenticate(request, username=username, password=password)

        if logged_in is not None:
            login(request, logged_in)
            return redirect('home')      
        else:
            messages.info(request, "Username and password doesn't match ")

    return render(request, 'login.html')


def signup_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is Taken')
            return redirect('signup_page')

        if password == password2:
            # Use create_user to handle password hashing
            new_user = User.objects.create_user(username=username, password=password)

            new_profile = models.Profile(user=new_user)
            new_profile.save()

            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            messages.error(request, "Passwords don't match, try again.")

    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'Succesfully Logged Out.')
    return redirect('login_page')