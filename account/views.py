from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def login_view(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_view')
    return render(request, 'accounts/login_view.html')


def signup_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        new_user = User.objects.create_user(username=username, password=password)
        return redirect('home')
    return render(request, 'accounts/signup_view.html')


def logout_view(request):
    logout(request)
    return redirect('home')
