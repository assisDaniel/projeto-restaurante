from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataUpdate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f'{self.nome}'