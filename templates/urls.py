from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index ),
    path('services/',services, name='services' ),
    path('search/',search,name='search' ),
]
