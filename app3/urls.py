from django.urls import path
from .views import home,customer,product

urlpatterns=[
    path('',home),
    path('customer3/',customer),
    path('product3/',product),
]