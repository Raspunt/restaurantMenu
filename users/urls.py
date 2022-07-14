
from django.contrib import admin
from django.urls import path


from . views import *

urlpatterns = [
    path('Register/',RegisterPage,name="RegisterUrl"),
    path('Login/',LoginPage,name="LoginUrl")
]