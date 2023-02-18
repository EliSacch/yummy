from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    ingedients = models.JSONField()
    procedure = ArrayField(models.TextField(max_length=200))
    servings = models.IntegerField()
    prepation_time = models.JSONField(blank=True, null=True)
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

