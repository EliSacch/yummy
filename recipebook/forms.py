from django import forms
from django.forms import MultiWidget, TextInput, BaseModelFormSet
from django.forms.models import inlineformset_factory
from .models import Recipe, Ingredient

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
