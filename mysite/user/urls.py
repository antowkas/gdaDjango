from django.urls import path, include
from .views import  user_login, register, logout_view


app_name = "users"


urlpatterns = [
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_view, name="logout")
]

