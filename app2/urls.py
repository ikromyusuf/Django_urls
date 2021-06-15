from django.urls import path
from .views import home2,customer2,product2

urlpatterns=[
    path('',home2),
    path('customer2/',customer2),
    path('product2/',product2),
]