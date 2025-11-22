from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect

def home(request):
    return redirect('/template')

def pruebas(request):
    return HttpResponse("Bienvenido a Django desde unitecnar")

def template_view(request):
    return render(request, 'index.html')
