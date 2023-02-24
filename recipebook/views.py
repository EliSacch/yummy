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
        all_recipes = Recipe.objects.filter(user=self.request.user)
        random_recipes = all_recipes.order_by('?')[:2]
        context = {
            'suggestions' : random_recipes
            }
        return context


class AddNewRecipeView(generic.CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'procedure', 'servings', 'preparation_time', 'tags', 'notes']
    template_name = 'add_recipe.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AddNewRecipeView, self).get_context_data(**kwargs)
        context = {
            'servings_range' : range(1,25)
            }
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.tags = self.request.POST.get('tags').strip("").split('#')
        return super(AddNewRecipeView, self).form_valid(form)