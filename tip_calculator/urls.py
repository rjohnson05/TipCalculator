"""
URL configuration for tip_calculator project.

The `urlpatterns` list routes URLs to views.

Author: Ryan Johnson
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("calculator.urls")),
    path('admin/', admin.site.urls),
]
