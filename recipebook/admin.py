from django.contrib import admin
from .models import Recipe, Ingredient, UserProfileImage

""" This is the admin.py file for the recipebook app. It is used to register the Recipe model with the admin site."""

# The following code to filter the recipes by tag in the admin page is taken from the following link: https://bradmontgomery.net/blog/django-admin-filters-arrayfields/
class ArrayFieldListFilter(admin.SimpleListFilter):
    """This is a list filter based on the values
    from a model's `tags` ArrayField. """

    title = 'Tags'
    parameter_name = 'tags'

    def lookups(self, request, model_admin):
        tags = Recipe.objects.values_list("tags", flat=True)
        tags = [(kw, kw) for sublist in tags for kw in sublist if kw]
        tags = sorted(set(tags))
        return tags

    def queryset(self, request, queryset):
        lookup_value = self.value() 
        if lookup_value:
            queryset = queryset.filter(tags__contains=[lookup_value])
        return queryset
# End of code from the above link


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('difficulty', 'created_on', ArrayFieldListFilter)
    readonly_fields = ('created_on', 'modified_on', 'user', 'pk')


@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    list_filter = ('name', 'recipe')
    readonly_fields = ('updated_on',)


@admin.register(UserProfileImage)
class UserProfileImageAdmin(admin.ModelAdmin):
    list_filter = ('user', 'profile_image')