from django.db import models
import re

class Reserva(models.Model):
    nomeCompleto = models.CharField('Nome Completo', max_length=600)
    email = models.EmailField('E-mail', help_text='exemplo@exemplo.com')
    telefone = models.CharField('Telefone', max_length=17, help_text='(00) 90000 - 0000')
    dataReserva = models.DateField('Data da Reserva')
    horaReserva = models.TimeField('Hora da Reserva')
    numPessoas = models.IntegerField('Número de Pessoas')
    mensagem = models.TextField('Mensagem', blank=True, null=True)
    pendente = models.BooleanField('Pendente', default=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataUpdate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'{self.nomeCompleto} - {self.dataReserva} | {self.horaReserva}'
    
    def save(self, *args, **kwargs):
        regex = r'\(?(\d{2})\)?\s*9(\d{4})[-\s]?(\d{4})'
        replacement = r'(\1) 9\2 - \3'
        if self.telefone:
            self.telefone = re.sub(regex, replacement, self.telefone)
        super().save(*args, **kwargs)
   