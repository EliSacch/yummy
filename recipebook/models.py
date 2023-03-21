from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    procedure = ArrayField(models.TextField(max_length=200), blank=True, null=True)
    servings = models.IntegerField()
    preparation_time = models.JSONField(blank=True, null=True)
    difficulty = models.IntegerField(blank=True, null=True)
    image = CloudinaryField('image', default='placeholder')
    tags = ArrayField(models.CharField(max_length=200))
    notes = models.TextField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add= True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def recipe_tags(self):
        tags = self.tags.join(', ')
        return tags
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, blank=False, null=False, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    
    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.name
    

class UserProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_image')
    profile_image = CloudinaryField('image', default=None, blank=True, null=True)

    def __str__(self):
        return self.user.username

