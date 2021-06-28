from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import View

from .forms import (
    IngredientFormSet,
    IngredientFormSetHelper,
    RecipeForm,
    StepFormSet,
    StepFormSetHelper,
)
from .models import Recipe


# class RecipeCreate(CreateView):
#     model = Recipe
#     form_class = RecipeForm


class RecipeCreate(View):
    template_name = "instructions/recipe_form.html"

    def get(self, request, *args, **kwargs):
        context = {
            "recipe_form": RecipeForm(),
            "ingredient_form_set": IngredientFormSet(prefix="ingredient"),
            "ingredient_helper": IngredientFormSetHelper(),
            "step_form_set": StepFormSet(prefix="step"),
            "step_helper": StepFormSetHelper(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {
            "recipe_form": RecipeForm(request.POST),
            "ingredient_form_set": IngredientFormSet(request.POST, prefix="ingredient"),
            "ingredient_helper": IngredientFormSetHelper(),
            "step_form_set": StepFormSet(request.POST, prefix="step"),
            "step_helper": StepFormSetHelper(),
        }
        return render(request, self.template_name, context)


class RecipeDetail(DetailView):
    model = Recipe
