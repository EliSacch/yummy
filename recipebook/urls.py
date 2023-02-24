from .import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('add_recipe/', views.AddNewRecipeView.as_view(), name='add_recipe'),
    path('my-recipes/', views.RecipeListView.as_view(), name='my_recipes'),
]