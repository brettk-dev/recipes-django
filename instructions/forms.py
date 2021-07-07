from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Hidden, Layout
from django.forms.models import ModelForm, inlineformset_factory

from .models import Ingredient, Recipe, Step


IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient, fields=["qty", "unit", "name"], extra=1)


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


StepFormSet = inlineformset_factory(
    Recipe, Step, fields=["number", "description"], extra=1)


class StepFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_class = "col-auto"
        self.layout = Layout(
            Field("number", type="hidden"),
            Div(FloatingField("description"), css_class="col-10"),
        )
        self.form_tag = False


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(FloatingField("name"))
        self.helper.form_tag = False
