from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home2(request):

    return HttpResponse("<h1 style='color:blue;text-align:center'>home app2</h1>")

def product2(request):
    
    return HttpResponse("<h1 style='color:blue;text-align:left'>product2</h1>")

def customer2(request):
    
    return HttpResponse("<h1 style='color:blue;text-align:left'>customer2</h1>")