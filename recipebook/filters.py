import django_filters
from .models import Recipe, Ingredient


class CharArrayFilter(django_filters.BaseCSVFilter, django_filters.CharFilter):
     pass

class RecipeFilter(django_filters.FilterSet):

    DIFFICULTY_CHOICES = (
        ('1', 'Easy'),
        ('2', 'Medium'),
        ('3', 'Hard'),
    )

    title = django_filters.CharFilter(lookup_expr='icontains')
    difficulty = django_filters.ChoiceFilter(choices=DIFFICULTY_CHOICES)
    tags = CharArrayFilter(field_name='tags', lookup_expr='contains')

    class Meta:
        model = Recipe
        fields = ['title', 'tags', 'difficulty']

class IngredientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ingredient
        fields = ['name',]

