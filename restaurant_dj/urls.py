from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('restoran.urls')),
    path('',include('users.urls'))
    
]
