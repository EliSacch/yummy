from .import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
]