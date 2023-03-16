from django.shortcuts import render,HttpResponse
from .import models

# Create your views here.
def index (request):
    return HttpResponse('I just cant help falling in Love with Jesus')

def index (request):
    return render(request, 'index.html')

def index (request):
    return render(request, "about.html")       