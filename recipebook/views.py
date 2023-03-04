from django.views import generic, View
from django .views.generic.edit import UpdateView, DeleteView

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientsForm, IngredientFormSet


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
    form_class = RecipeForm
    formset = IngredientFormSet(queryset=Ingredient.objects.none())
    template_name = 'add_recipe.html'

    def get_context_data(self, **kwargs):
        context = super(AddNewRecipeView, self).get_context_data(**kwargs)
        context['formset'] = IngredientFormSet(queryset=Ingredient.objects.none())
        return context

    """def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        #formset = IngredientFormSet(request.POST)
        #if form.is_valid() and formset.is_valid():
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = self.request.user
            recipe.save()
            
            ingredients = formset.save(commit=False)
            
            for ingredient in ingredients:
                ingredient.recipe = recipe
                ingredient.save()
                
            messages.success(self.request, 'Ingredient added successfully!')
        
        else:
            messages.error(self.request, 'Error adding recipe')
            form = RecipeForm()
            #formset = IngredientFormSet(queryset=Ingredient.objects.none())

        return form.is_valid()"""
    
    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.user = self.request.user
        recipe.save()
        messages.success(self.request, 'Ingredient added successfully!')
        
        return super().form_valid(form)
    

    def get_success_url(self):
        return reverse("recipe_detail", args=[self.object.pk])


# View for the recipe update page
class EditRecipeView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    ingredients_form_class = IngredientsForm
    template_name = 'edit_recipe.html'

    def get_context_data(self, **kwargs):
        context = super(EditRecipeView, self).get_context_data(**kwargs)
        context = {
            'form': RecipeForm(instance=self.object),
            'recipe' : self.object,
            'pk' : self.object.pk
        }
        return context
    
    def get_success_url(self):
        return reverse("recipe_detail", args=[self.object.pk])
    
