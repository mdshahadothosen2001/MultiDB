from django.contrib import admin
from django.apps import apps

from django_mongodb_engine.contrib import MongoDBManager

Integredient = apps.get_model('calories', 'Integredient')

@admin.register(Integredient)
class IntegredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories')
    search_fields = ('name',)

    def get_queryset(self, request):
        return Integredient.objects.using('mongodb').all()
