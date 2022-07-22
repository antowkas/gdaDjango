from django.urls import path
from .views import index, airports, date_time_filter, passanger


app_name = "flight"


urlpatterns = [
    path("index/", index),
    path("airports/", airports),
    path("date_filter/", date_time_filter, name="date_filter"),
    path("passenger/<slug>", passanger),
]
