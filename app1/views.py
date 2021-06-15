from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    return HttpResponse("<h1 style='color:blue;text-align:center'>home</h1>")

def product(request):
    
    return HttpResponse("<h1 style='color:blue;text-align:left'>product1</h1>")

def customer(request):
    
    return HttpResponse("<h1 style='color:blue;text-align:left'>customer1</h1>")