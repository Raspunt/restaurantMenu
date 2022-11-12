from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . views import *

urlpatterns = [
    path('',WellcomePage,name="MainPageUrl"),
    path('menu/',MainPage,name="WellcomePageUrl"),
    path('CategoryCreate/',CategoryCreate,name="CategoryCreateUrl"),
    path('ProductCreate/',ProductCreate,name="ProductCreateUrl"),
    path('Category/<int:category_id>/',CategoryDetail,name="CategoryDetailUrl"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
