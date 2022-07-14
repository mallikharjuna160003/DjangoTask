from django.contrib import admin
from django.urls import path,include
from .views import index

urlpatterns = [
    path('index/',index),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]