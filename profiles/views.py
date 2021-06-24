from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from profiles.forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render


@login_required
def profile(request):
    return render(request, "profiles/profile.html")


class Register(CreateView):
    template_name = "profiles/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("profiles:login")


class Login(LoginView):
    template_name = "profiles/login.html"
    form_class = LoginForm
