from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

# Create your views here.

def index_view(request):
    return render(request, 'accounts/index.html')

def register_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/register.html')

    elif request.method == 'POST':
        payload={
                "username" : request.POST.get('user_name'),
                "first_name" : request.POST.get('first_name'),
                "last_name" : request.POST.get('last_name'),
                "email" : request.POST.get('email'),
                "password" : request.POST.get('password'),
                }
        user = User.objects.create(**payload)
        user.set_password(payload.get('password'))
        user.save()
        login(request,user)

        return redirect('/accounts/home')

    
def login_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')

    elif request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return render(request, 'accounts/index.html')
        return redirect('/accounts/login')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login')
