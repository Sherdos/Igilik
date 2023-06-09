from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index ),
    path('search/',search,name='search' ),
]
