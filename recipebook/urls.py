from .import views
from django.urls import path
#from django_filters.views import FilterView
#from .models import Recipe


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add_recipe/', views.AddNewRecipeView.as_view(), name='add_recipe'),
    path('recipe/<int:pk>/edit', views.EditRecipeView.as_view(), name='edit_recipe'),
    path('my_recipes/', views.RecipeListView.as_view(), name='my_recipes'),
    #path('my_recipes/', FilterView.as_view(model=Recipe), name='my_recipes'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/delete', views.DeleteRecipeView.as_view(), name='delete_recipe'),
]