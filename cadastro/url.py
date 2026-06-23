from django.urls import path
from .views import teste, cadastro

urlpatterns = [
    path('teste/', teste),
    path('cadastro/', cadastro, name='cadastrar')
]