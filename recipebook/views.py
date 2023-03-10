from django.views import generic, View
from django .views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin # to select 1 item from db

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
class AddNewRecipeView(generic.CreateView, SingleObjectMixin):
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    
    def get_context_data(self, **kwargs):
        context = super(AddNewRecipeView, self).get_context_data(**kwargs)
        context = {
            'form': RecipeForm(instance=self.object or None),
            'formset' : IngredientFormSet(queryset=Ingredient.objects.none()),
        }
        return context
    
    def get(self, request, *args, **kwargs):
        form = RecipeForm()
        formset = IngredientFormSet(queryset=Ingredient.objects.none())
        return render(request, 'add_recipe.html', {'form': form, 'formset': formset})
    
    def post(self, request, *args, **kwargs):
        form = RecipeForm(self.request.POST)
        
        if form.is_valid():
            print('form is valid')
            recipe = form.save(commit=False)
            formset = IngredientFormSet(self.request.POST, instance=recipe)
            if formset.is_valid():
                print('formset is valid')
                recipe.user = self.request.user
                recipe.save()

                formset.save(commit=False)
                for ingredient in formset:
                    if ingredient.cleaned_data.get('name') is not None:
                        ingredient.recipe = recipe
                        ingredient.save()
                        print(ingredient.cleaned_data.get('name') + ' added to recipe')
                    else:
                        pass
            else:
                print('formset is invalid')
                for error in formset.errors:
                    messages.error(self.request, error)
                return super().form_invalid(form)
            
            messages.success(self.request, 'Recipe added successfully!')
            print(request.POST)
            return super().form_valid(form)
        else:
            for error in form.errors:
                messages.error(self.request, error)
            return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Recipe updated successfully!')
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})



# View for the recipe update page
class EditRecipeView(UpdateView, SingleObjectMixin):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'


    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super(EditRecipeView, self).get_context_data(**kwargs)
        context = {
            'form': RecipeForm(instance=self.object),
            'formset' : IngredientFormSet(instance=self.object),
        }
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = RecipeForm(self.request.POST, instance=self.object) 
        
        if form.is_valid():
            print('form is valid')
            recipe = form.save(commit=False)
            formset = IngredientFormSet(self.request.POST, instance=recipe)
            if formset.is_valid():
                print('formset is valid')
                recipe.user = self.request.user
                recipe.save()

                formset.save(commit=False)
                for ingredient in formset:
                    if ingredient in formset.deleted_forms:
                        ingredient.instance.delete()
                    elif ingredient.cleaned_data.get('name') is not None:
                        ingredient.instance.recipe = recipe
                        ingredient.save()
                    else:
                        pass
            else:
                print('formset is invalid')
                for error in formset.errors:
                    print(error)
                    print('error')
                    messages.error(self.request, error)
                return super().form_invalid(form)
            
            messages.success(self.request, 'Recipe updated successfully!')
            return super().form_valid(form)
        else:
            for error in form.errors:
                messages.error(self.request, error)
            return super().form_invalid(form)
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Recipe updated successfully!')
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})