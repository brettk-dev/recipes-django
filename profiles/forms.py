from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.contrib.auth.models import User
from django.forms import models


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField(
                "first_name", "last_name", "email", "username", "password1", "password2"
            )
        )
        self.helper.form_tag = False


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(FloatingField("username", "password"))
        self.helper.form_tag = False
