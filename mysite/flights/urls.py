from django.urls import path
from .views import index, airports


urlpatterns = [
    path("index/", index),
    path("airports/", airports),
]
