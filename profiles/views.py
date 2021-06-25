from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from profiles.forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render


@login_required
def profile(request):
    full_name = f"{request.user.first_name} {request.user.last_name}"
    return render(request, "profiles/profile.html", {"title": full_name})


class Register(CreateView):
    template_name = "profiles/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("profiles:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Register"
        return context


class Login(LoginView):
    template_name = "profiles/login.html"
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context
