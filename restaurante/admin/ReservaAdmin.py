from django.contrib import admin

from restaurante import models

@admin.register(models.Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomeCompleto', 'email', 'telefone', 'dataReserva', 'horaReserva', 'numPessoas', 'mensagem', 'pendente')
    list_display_links = ('id', 'nomeCompleto', 'email')
    list_editable = ('pendente',)
    readonly_fields = ('pendente', 'dataCriacao', 'dataUpdate')

# Register your models here.
