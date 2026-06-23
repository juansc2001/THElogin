from django.shortcuts import render

# Create your views here.

def teste(request):
    return render(request, 'teste.html')

def cadastro(request):
    return render(request, 'cadastro.html')