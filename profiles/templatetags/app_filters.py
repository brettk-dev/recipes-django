from django.contrib.auth.forms import AuthenticationForm
from django import template
from pprint import pprint


register = template.Library()


@register.filter(name="bootstrap")
def boostrap(form):
    if type(form) != AuthenticationForm:
        return

    form.fields["username"].widget.attrs["class"] = "form-control"
    form.fields["password"].widget.attrs["class"] = "form-control"
    pprint(vars(form.fields["username"].label_tag()))

    return form
