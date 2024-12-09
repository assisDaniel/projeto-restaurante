from django.db import models

class Cardapio(models.Model):
    nome = models.CharField('Nome do Item', max_length=100, unique=True)
    descricao = models.CharField('Descrição', max_length=600)
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2)
    imagem = models.ImageField('Imagem do Item')
    categoria = models.ForeignKey('Categoria', verbose_name='Categoria', on_delete=models.PROTECT)
    dataCriacao = models.DateTimeField(auto_now_add=True)
    dataUpdate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cardápio'
        verbose_name_plural = 'Cardápio'

    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'
