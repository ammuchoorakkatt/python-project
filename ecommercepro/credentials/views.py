from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentials.models import User_details


def home(request):
    return render(request,"home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "email id/username already taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('credentials:login')
            messages.info(request,'user created')
        else:
             messages.info(request, "password doesn't match")
             return redirect('credentials:register')
        return redirect('/')

    return render(request,"register.html")


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('shop/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('credentials:login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('credentials:home')