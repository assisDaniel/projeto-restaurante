# Generated by Django 5.1.4 on 2024-12-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0004_alter_cardapio_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='imagem',
            field=models.ImageField(upload_to='restaurante_teste/static/img/menu/', verbose_name='Imagem do Item'),
        ),
    ]