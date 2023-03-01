from django import forms
from django.forms import MultiWidget, TextInput
from django.forms.models import inlineformset_factory
from betterforms.multiform import MultiModelForm
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    servings = forms.IntegerField(widget=forms.Select(choices=[(i, i) for i in range(1, 25)]))
    class Meta:
        model = Recipe
        fields = ['title', 'procedure', 'servings', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'amount', 'unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#RecipeIngredientsFormset = inlineformset_factory(Recipe, Ingredient, fields=('name', 'amount', 'unit'), extra=1, can_delete=True)