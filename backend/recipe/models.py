from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    integredient = models.PositiveSmallIntegerField()
    calories = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
        db_table = "recipe"
