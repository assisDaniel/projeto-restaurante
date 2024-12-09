from django.contrib import admin

from restaurante import models

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    readonly_fields = ('dataCriacao', 'dataUpdate')

# Register your models here.
