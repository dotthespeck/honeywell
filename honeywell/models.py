from __future__ import unicode_literals

from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    dish = models.CharField(max_length=200)
    main_ingredient = models.CharField(max_length=200)
    other_ingredients = models.CharField(max_length=500)

    def __str__(self):
        return self.title
