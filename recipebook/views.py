from django.shortcuts import render
from django.views import generic
from .models import Recipe


class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 12
    

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        all_recipes = Recipe.objects.all()
        context['suggestions'] = all_recipes.order_by('?')[:2]
        return context

