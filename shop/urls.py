
from django.contrib import admin
from django.urls import path, include

from shop import views

urlpatterns = [
    path('fill-database/', views.fill_database, name='fill-database'),

]
