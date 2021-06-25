from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput

from .models import Ingredient, Recipe, Step


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(FloatingField("name"))
        self.helper.form_tag = False


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ["qty", "unit", "name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(FloatingField("qty"), css_class="col-2"),
            Div(FloatingField("unit"), css_class="col-3"),
            Div(FloatingField("name"), css_class="col-7"),
        )
        self.helper.form_tag = False


class StepForm(ModelForm):
    class Meta:
        model = Step
        fields = ["number", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "col-auto"
        self.helper.layout = Layout(
            Field("number", type="hidden"),
            Div(FloatingField("description"), css_class="col-10"),
        )
        self.helper.form_tag = False
