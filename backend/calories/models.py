from django.db import models


class Integredient(models.Model):
    name = models.CharField(max_length=20)
    calories = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Integredient"
        verbose_name_plural = "Integredients"
        db_table = "integredient"
        app_label = 'calories'
