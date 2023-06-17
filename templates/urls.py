from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index' ),
    path('orders/',orders, name='orders' ),
    path('search/',search,name='search' ),
]
