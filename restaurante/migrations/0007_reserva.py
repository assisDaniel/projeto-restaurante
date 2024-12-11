# Generated by Django 5.1.4 on 2024-12-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0006_alter_cardapio_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=600, verbose_name='Nome Completo')),
                ('email', models.EmailField(help_text='exemplo@exemplo.com', max_length=254, unique=True, verbose_name='E-mail')),
                ('telefone', models.CharField(help_text='90000-0000', max_length=16, unique=True, verbose_name='Telefone')),
                ('dataReserva', models.DateField(verbose_name='Data da Reserva')),
                ('horaReserva', models.TimeField(verbose_name='Hora da Reserva')),
                ('numPessoas', models.IntegerField(max_length=2, verbose_name='Número de Pessoas')),
                ('mensagem', models.TextField(blank=True, null=True, verbose_name='Mensagem')),
                ('pendente', models.BooleanField(default=True, verbose_name='Pendente')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('dataUpdate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]
