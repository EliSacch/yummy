from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django .views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse
from .models import Recipe
from .forms import RecipeForm


# General view for the home page
class HomeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 12
    

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            all_recipes = Recipe.objects.filter(user=self.request.user)
            random_recipes = all_recipes.order_by('?')[:5]
            context = {
                'all_recipes' : all_recipes,
                'suggestions' : random_recipes
                }
        return context


# View for the my recipes page that displays all the reciepes created by the user
class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('created_on')
    template_name = 'my_recipes.html'
    paginate_by = 12
    

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            all_recipes = Recipe.objects.filter(user=self.request.user)
            context = {
                'all_recipes' : all_recipes
                }
        return context


# View for the recipe detail page
class RecipeDetailView(View):
    
    def get(self, request, pk, *args, **kwargs):
        if self.request.user.is_authenticated:
            queryset = Recipe.objects.filter(user=self.request.user)
            recipe = get_object_or_404(queryset, pk=pk)

            return render(
                request,
                'recipe_detail.html',
                {
                    'recipe' : recipe
                }
            )


# View for the recipe creation page
class AddNewRecipeView(generic.CreateView):
    model = Recipe
    fields = ['title', 'ingredients', 'procedure', 'servings', 'preparation_time', 'tags', 'notes']
    template_name = 'add_recipe.html'

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
    
    def get_success_url(self):
        return reverse("recipe_detail", args=[self.object.pk])
    

# View for the recipe creation page
class EditRecipeView(UpdateView):
    model = Recipe
    template_name = 'edit_recipe.html'
    form_class = RecipeForm
    success_url = '/thanks/'

    def get_context_data(self, **kwargs):
        context = super(EditRecipeView, self).get_context_data(**kwargs)
        context = {
            'form' : RecipeForm(instance=self.object)
            }
        return context
    
    def get_success_url(self):
        return reverse("recipe_detail", args=[self.object.pk])
    