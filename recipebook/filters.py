import django_filters
from .models import Recipe

class RecipeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    difficulty = django_filters.NumberFilter(lookup_expr='exact')
    class Meta:
        model = Recipe
        fields = {
            'title': ['icontains'],
            'difficulty': ['exact'],
            
        }
