from django.test import TestCase
from .models import User, Recipe, Ingredient, UserProfileImage 

class TestModels(TestCase):

    def test_user_model(self):
        user = User.objects.create_user(username='test', password='test')
        self.assertEqual(user.username, 'test')

    def test_recipe_model(self):
        user = User.objects.create_user(username='test', password='test')
        recipe = Recipe.objects.create(title='Test Recipe', user=user, procedure=['step1', 'step2'], servings=2, difficulty=1, tags=['test', 'test2'])
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.user, user)
        self.assertEqual(recipe.procedure, ['step1', 'step2'])
        self.assertEqual(recipe.servings, 2)
        self.assertEqual(recipe.difficulty, 1)
        self.assertEqual(recipe.tags, ['test', 'test2'])
        self.assertEqual(recipe.image, 'placeholder')

    def test_ingredient_model(self):
        user = User.objects.create_user(username='test', password='test')
        recipe = Recipe.objects.create(title='Test Recipe', user=user, procedure=['step1', 'step2'], servings=2, difficulty=1, tags=['test', 'test2'])
        ingredient = Ingredient.objects.create(name='Test Ingredient', amount=2, recipe=recipe)
        self.assertEqual(ingredient.name, 'Test Ingredient')
        self.assertEqual(ingredient.amount, 2)
        self.assertEqual(ingredient.recipe, recipe)

    def test_user_profile_image_model(self):
        user = User.objects.create_user(username='test', password='test')
        image = UserProfileImage.objects.create(user=user, profile_image='test.jpg')
        self.assertEqual(image.user, user)
        self.assertEqual(image.profile_image, 'test.jpg')