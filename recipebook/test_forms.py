from django.test import TestCase
from .forms import RecipeForm, IngredientsForm, StepsForm, RecipeSearchForm, UserProfileForm, UserProfileImageForm, UserDeleteForm

class TestRecipeForm(TestCase):
    def test_title_is_required(self):
        form = RecipeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def procedure_is_not_required(self):
        form = RecipeForm({'procedure': ''})
        self.assertTrue(form.is_valid())

    def test_servings_is_required(self):
        form = RecipeForm({'servings': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('servings', form.errors.keys())
        self.assertEqual(form.errors['servings'][0], 'This field is required.')

    def test_tags_is_required(self):
        form = RecipeForm({'tags': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('tags', form.errors.keys())
        self.assertEqual(form.errors['tags'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = RecipeForm()
        self.assertEqual(form.Meta.fields, ['title', 'image', 'procedure', 'servings', 'preparation_time', 'difficulty', 'tags', 'notes', ])


class TestIngredientsForm(TestCase):
    def test_name_is_required(self):
        form = IngredientsForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_amount_is_required(self):
        form = IngredientsForm({'amount': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors.keys())
        self.assertEqual(form.errors['amount'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = IngredientsForm()
        self.assertEqual(form.Meta.fields, ['name', 'amount', 'unit'])

    
class TestStepsForm(TestCase):
    def test_step_is_not_required(self):
        form = StepsForm({'step': ''})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = StepsForm()
        self.assertEqual(form.Meta.fields, ['step', ])


class TestRecipeSearchForm(TestCase):
    def test_search_is_not_required(self):
        form = RecipeSearchForm({'search': ''})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = RecipeSearchForm()
        self.assertEqual(form.Meta.fields, ['search', ])


class TestUserProfileForm(TestCase):
    def test_username_is_required(self):
        form = UserProfileForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.fields, ['username',])


class TestUserProfileImageForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserProfileImageForm()
        self.assertEqual(form.Meta.fields, ['profile_image',])


class TestUserDeleteForm(TestCase):
    def test_delete_is_required(self):
        form = UserDeleteForm({'delete': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('delete', form.errors.keys())
        self.assertEqual(form.errors['delete'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = UserDeleteForm()
        self.assertEqual(form.Meta.fields, ['delete',])