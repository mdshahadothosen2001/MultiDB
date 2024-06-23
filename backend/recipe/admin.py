from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title",)
    list_per_page = 10


admin.site.register(Recipe, RecipeAdmin)
