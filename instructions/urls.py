from django.urls import path

from . import views


app_name = "recipes"
urlpatterns = [
    path("new", views.RecipeCreate.as_view(), name="create"),
    path("<int:pk>", views.RecipeDetail.as_view(), name="details"),
    path("", views.RecipeList.as_view(), name="list"),
]
