from django.views import generic, View
from django .views.generic.edit import UpdateView, DeleteView
from django .views.generic.detail import SingleObjectMixin

from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientsForm


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
class AddNewRecipeView(generic.CreateView, SingleObjectMixin):
    model = Recipe
    form_class = RecipeForm
    ingredients_form_class = IngredientsForm
    template_name = 'add_recipe.html'

    def get_context_data(self, **kwargs):
        context = super(AddNewRecipeView, self).get_context_data(**kwargs)
        context = {
            'form': RecipeForm(instance=self.object),
            'ingredients_form': IngredientsForm(instance=self.object)
        }
        return context
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(None)
        ingredients_form = self.ingredients_form_class(None)
        return render(request, self.template_name, {'form': form, 'ingredients_form': ingredients_form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        ingredients_form = self.ingredients_form_class(request.POST)
        if form.is_valid() and ingredients_form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = self.request.user
            # Here we split the tags string into a list and remove any empty strings
            raw_tags = self.request.POST.get('tags').lower().replace(" ", "#").split('#')
            form.instance.tags = [x.strip() for x in raw_tags if x.strip() != '']
            recipe.save()
            ingredients = ingredients_form.save(commit=False)
            ingredients.recipe = recipe
            ingredients.save()

            messages.add_message(self.request, messages.SUCCESS, 'Recipe added successfully')

            return super(AddNewRecipeView, self).form_valid(form)

        else:
            messages.add_message(self.request, messages.ERROR, 'There was an error adding your recipe. Please try again.')
            return render(request, self.template_name, {'form': form, 'ingredients_form': ingredients_form})

    def get_success_url(self):
        return reverse("recipe_detail", args=[self.object.pk])


# View for the recipe update page
class EditRecipeView(UpdateView, SingleObjectMixin):
    model = Recipe
    form_class = RecipeForm
    ingredients_form_class = IngredientsForm
    template_name = 'edit_recipe.html'

    def get_context_data(self, **kwargs):
        context = super(EditRecipeView, self).get_context_data(**kwargs)
        context = {
            'form': RecipeForm(instance=self.object),
            'ingredients_form': IngredientsForm(instance=self.object),
            'pk' : self.kwargs['pk']
        }
        return context
    
    def get_success_url(self):
            return reverse("recipe_detail", args=[self.object.pk])
    
