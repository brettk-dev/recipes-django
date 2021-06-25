from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import View

from .forms import IngredientForm, RecipeForm, StepForm
from .models import Recipe


# class RecipeCreate(CreateView):
#     model = Recipe
#     form_class = RecipeForm


class RecipeCreate(View):
    template_name = "instructions/recipe_form.html"

    def get(self, request, *args, **kwargs):
        context = {
            "recipe_form": RecipeForm(),
            "ingredient_forms": [IngredientForm()],
            "step_forms": [StepForm()],
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {
            "recipe_form": RecipeForm(),
            "ingredient_forms": [IngredientForm()],
            "step_forms": [StepForm()],
        }
        return render(request, self.template_name, context)


class RecipeDetail(DetailView):
    model = Recipe
