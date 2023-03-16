from django.views import generic, View
from django .views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin # to select 1 item from db

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientFormSet
from .filters import RecipeFilter


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
                'suggestions' : random_recipes,
                'difficulty_choices' : [(1, 'Easy'), (2, 'Medium'), (3, 'Hard')],
                'tags' : self.get_tags()
                }
        return context
    
    def get_tags(self):
        all_tags = Recipe.objects.filter(user=self.request.user).values_list('tags', flat=True).distinct()

        tags = []
        for tag in all_tags:
            for t in tag:
                if t not in tags:
                    tags.append(t)
                else:
                    pass
    
        return tags


# View for the my recipes page that displays all the reciepes created by the user
class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.all()
    template_name = 'my_recipes.html'
    context_object_name = 'all_recipes'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        self.filterset = RecipeFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context = {
                'difficulty_choices' : [(1, 'Easy'), (2, 'Medium'), (3, 'Hard')],
                'form' : self.filterset.form,
                'all_recipes' : self.filterset.qs,
                }
        return context


# View for the recipe detail page
class RecipeDetailView(View):
    
    def get(self, request, pk, *args, **kwargs):
        if self.request.user.is_authenticated:
            queryset = Recipe.objects.filter(user=self.request.user)
            recipe = get_object_or_404(queryset, pk=pk)
            difficulty_choices = [(1, 'Easy'), (2, 'Medium'), (3, 'Hard')]

            return render(
                request,
                'recipe_detail.html',
                {
                    'recipe' : recipe,
                    'difficulty_choices' : difficulty_choices
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
            recipe = form.save(commit=False)
            formset = IngredientFormSet(self.request.POST, instance=recipe)
            if formset.is_valid():
                recipe.user = self.request.user
                tags = form.cleaned_data.get('tags')[0].split(' ')
                tags_array = [tag for tag in tags]
                recipe.tags = tags_array
                
                recipe.save()

                formset.save(commit=False)
                for ingredient in formset:
                    if ingredient.cleaned_data.get('name') is not None:
                        ingredient.recipe = recipe
                        ingredient.save()
                    else:
                        pass
            else:
                print('formset is invalid')
                for error in formset.errors:
                    messages.error(self.request, error)
                return super().form_invalid(form)
            
            messages.success(self.request, 'Recipe added successfully!')
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
            'preparation_time' : self.object.preparation_time if self.object else None,
            'formset' : IngredientFormSet(instance=self.object),
        }
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = RecipeForm(self.request.POST, request.FILES, instance=self.object)
        
        if form.is_valid():
            recipe = form.save(commit=False)
            formset = IngredientFormSet(self.request.POST, self.request.FILES, instance=recipe)

            if formset.is_valid():
                recipe.user = self.request.user
                tags = form.cleaned_data.get('tags')[0].split(' ')
                recipe.tags = tags
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
    

class DeleteRecipeView(DeleteView):
    model = Recipe
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Recipe deleted successfully!')
        return super().delete(request, *args, **kwargs)