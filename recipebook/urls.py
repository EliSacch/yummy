from .import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('my-recipes/', views.RecipeListView.as_view(), name='my_recipes'),
]