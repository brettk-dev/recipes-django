from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from pprint import pprint

from .forms import (
    IngredientFormSet,
    IngredientFormSetHelper,
    RecipeForm,
    StepFormSet,
    StepFormSetHelper,
)
from .models import Recipe


class RecipeCreate(LoginRequiredMixin, View):
    template_name = "instructions/recipe_form.html"

    def get(self, request, *args, **kwargs):
        recipe = Recipe()
        context = {
            "recipe_form": RecipeForm(),
            "ingredient_form_set": IngredientFormSet(instance=recipe, prefix="ingredient"),
            "ingredient_helper": IngredientFormSetHelper(),
            "step_form_set": StepFormSet(instance=recipe, prefix="step"),
            "step_helper": StepFormSetHelper(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        recipe_form = RecipeForm(request.POST)
        ingredient_form_set = IngredientFormSet(
            request.POST, prefix="ingredient")
        step_form_set = StepFormSet(request.POST, prefix="step")
        print(step_form_set.errors)
        if (recipe_form.is_valid() and ingredient_form_set.is_valid() and step_form_set.is_valid()):
            recipe = recipe_form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            ingredients = ingredient_form_set.save(commit=False)
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()
            steps = step_form_set.save(commit=False)
            for step in steps:
                step.recipe = recipe
                step.save()
            return redirect(recipe)
        context = {
            "recipe_form": recipe_form,
            "ingredient_form_set": ingredient_form_set,
            "ingredient_helper": IngredientFormSetHelper(),
            "step_form_set": step_form_set,
            "step_helper": StepFormSetHelper(),
        }
        return render(request, self.template_name, context)


class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(pk=self.kwargs[self.pk_url_kwarg], user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context


class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My Recipes"
        return context
