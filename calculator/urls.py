from django.urls import path

from calculator import views

"""
This file contains the URL configuration for the calculator app, routing URLs to views.

Author: Ryan Johnson
"""

app_name = 'calculator'
urlpatterns = [
    path("", views.index, name="index"),
    path("/results/", views.results, name="results"),
]