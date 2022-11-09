from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("multiply", views.n_times_string, name="multiply"),
    path("test", views.test, name="test")
]