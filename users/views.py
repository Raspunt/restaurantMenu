
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse


def RegisterPage(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(username,email,password)

        return HttpResponse('1 user created')

    return render(request,'users/RegisterPage.html')


def LoginPage(request):

    if request.method == "POST":
        print(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)

        if user is not None:
            print('user exist')
            return HttpResponse('1 user exist')
        else:
            print('user does not exist')
            return HttpResponse('0 user does not exist')



    return render(request,'users/LoginPage.html')