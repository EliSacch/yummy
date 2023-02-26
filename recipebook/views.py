from django.shortcuts import render
from django.views import generic
from .models import Recipe

# General view for the home page
class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 12
    

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            all_recipes = Recipe.objects.filter(user=self.request.user)
            random_recipes = all_recipes.order_by('?')[:2]
            context = {
                'all_recipes' : all_recipes,
                'suggestions' : random_recipes
                }
        return context


# View for the recipe creation page
class AddNewRecipeView(generic.CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'procedure', 'servings', 'preparation_time', 'tags', 'notes']
    template_name = 'add_recipe.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(AddNewRecipeView, self).get_context_data(**kwargs)
        context = {
            # Here we pass the range of values for the servings field to the comtext(1-24)
            'servings_range' : range(1,25)
            }
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Here we split the tags string into a list and remove any empty strings
        raw_tags = self.request.POST.get('tags').lower().replace(" ", "#").split('#')
        form.instance.tags = [x.strip() for x in raw_tags if x.strip() != '']
        return super(AddNewRecipeView, self).form_valid(form)