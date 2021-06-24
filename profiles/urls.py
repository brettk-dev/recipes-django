from django.contrib.auth.views import LoginView
from django.urls import path

from . import views


appname = "profiles"
urlpatterns = [
    path("", views.profile, name="profile"),
    path("login/", views.Login.as_view(), name="login"),
]
