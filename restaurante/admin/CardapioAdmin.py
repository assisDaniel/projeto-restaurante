from django.contrib import admin

from restaurante import models

@admin.register(models.Cardapio)
class CardapioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria')
    list_display_links = ('id', 'nome')
    readonly_fields = ('dataCriacao', 'dataUpdate')

# Register your models here.
