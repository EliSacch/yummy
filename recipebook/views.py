from django.views import generic, View
from django .views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin # to select 1 item from db

from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.core.paginator import Paginator

from .models import Recipe, Ingredient, User, UserProfileImage
from .forms import RecipeForm, IngredientFormSet, RecipeSearchFrom, UserProfileForm, UserProfileImageForm, UserDeleteForm
from .filters import RecipeFilter


# General view for the home page
class HomeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.order_by('created_on')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        search_form = RecipeSearchFrom()
        if self.request.user.is_authenticated:
            all_recipes = Recipe.objects.filter(user=self.request.user)
            random_recipes = all_recipes.order_by('?')[:5]
            user_profile_image = UserProfileImage.objects.filter(user=self.request.user).first()

            context = {
                'all_recipes' : all_recipes,
                'suggestions' : random_recipes,
                'difficulty_choices' : [(1, 'Easy'), (2, 'Medium'), (3, 'Hard')],
                'tags' : self.get_tags(),
                'search_form' : search_form,
                'user_profile_image' : user_profile_image,
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
    
    
    def post(self, request, *args, **kwargs):
        #form = RecipeSearchFrom(request.GET)
        queryset = Recipe.objects.filter(user=self.request.user)

        if request.POST.get('action') == 'post':
            search_string = str(request.POST.get('search_string'))
            if search_string is not None:
                search_results = queryset.filter(title__icontains=search_string)
                data = serializers.serialize('json', list(search_results), fields=('pk','title'))

                return JsonResponse({'data' : data}, status=200)
            else:
                return JsonResponse({'data' : 'No results found'}, status=200)


# View for the my recipes page that displays all the reciepes created by the user
class RecipeListView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.all()
    template_name = 'my_recipes.html'
    context_object_name = 'all_recipes'

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user).order_by('created_on')
        self.filterset = RecipeFilter(self.request.GET, queryset=queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        # Pagination
        paginate = Paginator(self.filterset.qs, 6)
        page_number = self.request.GET.get('page')
        user_profile_image = UserProfileImage.objects.filter(user=self.request.user).first()

        if self.request.user.is_authenticated:
            context = {
                'difficulty_choices' : [(1, 'Easy'), (2, 'Medium'), (3, 'Hard')],
                'form' : self.filterset.form,
                'all_recipes' : paginate.get_page(page_number),
                'user_profile_image' : user_profile_image,
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
                messages.error(self.request, form.errors)
                return super().form_invalid(form)
            
            messages.success(self.request, 'Recipe added successfully!')
            return super().form_valid(form)
        else:
            messages.error(self.request, form.errors)
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
                messages.error(self.request, formset.errors)
                return super().form_invalid(form)
            
            messages.success(self.request, 'Recipe updated successfully!')
            return super().form_valid(form)
        else:
            messages.error(self.request, form.errors)
            return super().form_invalid(form)
    
    
    def form_valid(self, form):
        messages.success(self.request, 'Recipe updated successfully!')
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})
    

# View for the recipe delete page
class DeleteRecipeView(DeleteView):
    model = Recipe
    success_url = '/'
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Recipe deleted successfully!')
        return super().delete(request, *args, **kwargs)
    

# View for the user profile page
class ProfileView(FormView):
    model = User
    form_classes = {
        'user_details_form' : UserProfileForm,
        'user_image_form' : UserProfileImageForm,
    }
    template_name = 'account/profile.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.object = self.request.user
            user = self.request.user
            user_profile_image = UserProfileImage.objects.filter(user=user).first()

            return render(
                request,
                'account/profile.html',
                {
                    'user' : user,
                    'user_profile_image' : user_profile_image,
                    'user_details_form': UserProfileForm(instance=self.object if self.object else None),
                    'user_image_form': UserProfileImageForm(instance=user_profile_image),
                }
            )
        else:
            return HttpResponseRedirect('login')
        
    def post(self, request, *args, **kwargs):
        self.object = self.request.user
        form = UserProfileForm(self.request.POST, instance=self.object)

        user_profile_image = UserProfileImage.objects.filter(user=self.request.user).first()
        form_image = UserProfileImageForm(request.POST, self.request.FILES, instance=user_profile_image)

        if request.FILES:
            image = form_image.save(commit=False)
            image.user = self.request.user
            if form_image.is_valid():
                form_image.save()
                messages.success(self.request, 'Profile image updated successfully!')
                return super().form_valid(form_image)
            else:
                messages.error(self.request, form_image.errors)
                return super().form_invalid(form_image)
        
        else:
            if form.is_valid():
                form.save()
                messages.success(self.request, 'User details updated successfully!')
                return super().form_valid(form)
            else:
                print('form invalid')
                messages.error(self.request, form.errors)
                return HttpResponseRedirect(reverse('profile'))

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated updated successfully!')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile')


# Delete user view
class DeleteUserView(FormView):
    model = User
    form_class = UserDeleteForm
    template_name = 'account/profile.html'

    def post(self, request, *args, **kwargs):
        form = UserDeleteForm(self.request.POST, instance=self.request.user)


        