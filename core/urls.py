
from django.contrib import admin
from django.urls import path
from django.urls import path, include #me permite incluir urls de outros modulos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.url'))
]
