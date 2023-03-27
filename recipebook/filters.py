import django_filters
from .models import Recipe

"""
This is a custom filter for the tags field in the Recipe model. 
It is a CharField, but it is a comma-separated list of values. 
This filter allows us to search for recipes that contain a specific tag.
"""
class CharArrayFilter(django_filters.BaseCSVFilter, django_filters.CharFilter):
     pass


"""
This is the filter class for the Recipe model.
It allows us to filter the recipes by title, tags, and difficulty.
"""
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
