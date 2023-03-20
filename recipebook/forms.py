from django import forms
from django.forms import MultiWidget, TextInput, BaseModelFormSet
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient, User, UserProfileImage

class RecipeForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    servings = forms.IntegerField(widget=forms.Select(choices=[(i, i) for i in range(1, 25)]))
    preparation_time = forms.JSONField(widget=forms.HiddenInput, required=False)
    difficulty_choices = [('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')]
    difficulty = forms.IntegerField(widget=forms.RadioSelect(choices=difficulty_choices), required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'procedure', 'servings', 'preparation_time', 'difficulty', 'tags', 'notes', ]


class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'amount', 'unit']


IngredientFormSet = inlineformset_factory(Recipe, Ingredient, fields=('name','amount', 'unit'), extra=0, can_delete=True)


class RecipeSearchFrom(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search recipe...', 'data-toggle' : 'drop-down' }), required=False)
 

class UserProfileForm(forms.ModelForm):
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['username',]


class UserProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'hidden',}), required=False)
    class Meta:
        model = UserProfileImage
        fields = ['profile_image', ]


class UserDeleteForm(forms.Form):
    delete = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'delete-user-confirm'}), required=True)
    class Meta:
        model = User
        fields = ['delete', ]

