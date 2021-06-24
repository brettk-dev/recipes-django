from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views


app_name = "profiles"
urlpatterns = [
    path("", views.profile, name="profile"),
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
