from django.urls import path

from calculator import views

app_name = 'calculator'
urlpatterns = [
    path("", views.index, name="index"),
    path("/results/", views.results, name="results"),
]