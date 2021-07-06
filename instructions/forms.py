from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Hidden, Layout
from django.forms.models import ModelForm, modelformset_factory
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


IngredientFormSet = modelformset_factory(
    Ingredient, fields=["qty", "unit", "name"])


class IngredientFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = Layout(
            Div(
                Div(FloatingField("qty"), css_class="col-2"),
                Div(FloatingField("unit"), css_class="col-3"),
                Div(FloatingField("name"), css_class="col-7"),
                css_class="row mb-3 ingredient_forms",
            )
        )
        self.form_tag = False


StepFormSet = modelformset_factory(Step, fields=["number", "description"])


class StepFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = "col-auto"
        self.layout = Layout(
            Field("number", type="hidden"),
            Div(FloatingField("description"), css_class="col-10"),
        )
        self.form_tag = False
