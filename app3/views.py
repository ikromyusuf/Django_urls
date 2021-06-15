from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("<h1 style='color:green;text-align:center'>home app3</h1>")

def product(request):
    
    return HttpResponse("<h1 style='color:green;text-align:left'>product3</h1>")

def customer(request):
    
    return HttpResponse("<h1 style='color:green;text-align:left'>customer3</h1>")