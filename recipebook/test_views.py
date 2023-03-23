from django.test import TestCase
from .models import User, Recipe, Ingredient, UserProfileImage

class TestViews(TestCase):
    def test_get_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_get_all_recipes_page(self):
        User.objects.create_user(username="test", password="test")
        self.client.login(username='test', password='test')
        response = self.client.get("/my_recipes/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "my_recipes.html")
    
    def test_get_add_recipe_page(self):
        User.objects.create_user(username="test", password="test")
        self.client.login(username='test', password='test')
        response = self.client.get("/add_recipe/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "add_recipe.html")

    def test_get_edit_recipe_page(self):
        user = User.objects.create_user(username="test", password="test")
        self.client.login(username='test', password='test')
        recipe = Recipe.objects.create(title="Test Recipe", user=user, procedure=["step1", "step2"], servings=2, difficulty=1, tags=["test", "test2"])
        response = self.client.get(f"/recipe/{recipe.pk}/edit")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit_recipe.html")

    def test_get_recipe_detail_page(self):
        user = User.objects.create_user(username="test", password="test")
        self.client.login(username='test', password='test')
        recipe = Recipe.objects.create(title="Test Recipe", user=user, procedure=["step1", "step2"], servings=2, difficulty=1, tags=["test", "test2"])
        response = self.client.get(f"/recipe/{recipe.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipe_detail.html")

    def test_get_profile_page(self):
        User.objects.create_user(username="test", password="test")
        self.client.login(username='test', password='test')
        response = self.client.get("/account/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/profile.html")



