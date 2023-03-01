from django import forms
from django.forms import MultiWidget, TextInput
from .models import Recipe

class RecipeForm(forms.ModelForm):
    servings = forms.IntegerField(widget=forms.Select(choices=[(i, i) for i in range(1, 25)]))
    class Meta:
        model = Recipe
        fields = ['title', 'procedure', 'servings', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'amount', 'unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
