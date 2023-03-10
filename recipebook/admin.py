from django.contrib import admin
from .models import Recipe, Ingredient

""" This is the admin.py file for the recipebook app. It is used to register the Recipe model with the admin site."""

# The following code to filter the recipes by tag in the admin page is taken from the following link: https://bradmontgomery.net/blog/django-admin-filters-arrayfields/
class ArrayFieldListFilter(admin.SimpleListFilter):
    """This is a list filter based on the values
    from a model's `tags` ArrayField. """

    title = 'Tags'
    parameter_name = 'tags'

    def lookups(self, request, model_admin):
        # Very similar to our code above, but this method must return a
        # list of tuples: (lookup_value, human-readable value). These
        # appear in the admin's right sidebar

        tags = Recipe.objects.values_list("tags", flat=True)
        tags = [(kw, kw) for sublist in tags for kw in sublist if kw]
        tags = sorted(set(tags))
        return tags

    def queryset(self, request, queryset):
        # when a user clicks on a filter, this method gets called. The
        # provided queryset with be a queryset of Items, so we need to
        # filter that based on the clicked keyword.

        lookup_value = self.value()  # The clicked keyword. It can be None!
        if lookup_value:
            # the __contains lookup expects a list, so...
            queryset = queryset.filter(tags__contains=[lookup_value])
        return queryset
# End of code from the above link



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('difficulty', 'created_on', ArrayFieldListFilter)
    readonly_fields = ('created_on', 'modified_on', 'user')


@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    list_filter = ('name', 'recipe')
    readonly_fields = ('updated_on',)
