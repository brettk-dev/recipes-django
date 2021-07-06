from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse('recipes:details', args=(self.pk,))


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    qty = models.FloatField()
    unit = models.CharField(max_length=20)
    name = models.CharField(max_length=150)


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.TextField()
