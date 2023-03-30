from django.test import TestCase
from .models import User, Recipe, Ingredient, UserProfileImage

class TestHomeView(TestCase):
    # Before login
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_logged_in(self):
        User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_logged_out(self):
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_signup_page(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    # After login

    
    

class TestAddRecipeView(TestCase):

    def test_get_add_recipe_page(self):
        User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        response = self.client.get('/add_recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_add_recipe(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        response = self.client.post('/add_recipe/', {
            'title': 'Test Recipe',
            'user': user,
            'procedure': ['step1', 'step2'],
            'servings': 2,
            'difficulty': 1,
            'tags': ['test', 'test2']
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')


class TestEditRecipeView(TestCase):

    def test_get_edit_recipe_page(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        recipe = Recipe.objects.create(title='Test Recipe', user=user, procedure=['step1', 'step2'], servings=2, difficulty=1, tags=['test', 'test2'])
        response = self.client.get(f'/recipe/{recipe.pk}/edit')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')

    def test_edit_recipe(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        recipe = Recipe.objects.create(title='Test Recipe', user=user, procedure=['step1', 'step2'], servings=2, difficulty=1, tags=['test', 'test2'])
        response = self.client.post(f'/recipe/{recipe.pk}/edit', {
            'title': 'Edit Test Recipe',
            'procedure': ['step1', 'step2', 'step3'],
            'servings': 7,
            'difficulty': 2,
            'tags': ['test', 'edited']
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')


class TestDeleteRecipeView(TestCase):

    def test_delete_recipe(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        recipe = Recipe.objects.create(title='Test Recipe', user=user, procedure=['step1', 'step2'], servings=2, difficulty=1, tags=['test', 'test2'])
        response = self.client.get(f'/recipe/{recipe.pk}/delete')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'my_recipes.html')


class TestMyRecipesView(TestCase):

    def test_get_all_recipes_page(self):
        User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        response = self.client.get('/my_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_recipes.html')


class TestRecipeDetailView(TestCase):

    def test_get_recipe_detail_page(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        recipe = Recipe.objects.create(title='Test Recipe', user=user, procedure=['step1', 'step2'], servings=2, difficulty=1, tags=['test', 'test2'])
        response = self.client.get(f'/recipe/{recipe.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')


class TestProfileView(TestCase):

    def test_get_profile_page(self):
        User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        response = self.client.get('/account/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile.html')

    def test_delete_user(self):
        user = User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')
        response = self.client.get(f'/account/profile/{user.pk}/delete')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'account/profile.html')
