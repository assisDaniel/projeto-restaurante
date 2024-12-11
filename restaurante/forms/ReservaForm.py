from django import forms
from restaurante.models import Reserva


class ReservasForm(forms.ModelForm):
    class Meta:
        model = Reserva
        exclude = [
            'pendente',
        ]

        labels = {
            'nomeCompleto' : 'Nome Completo',
            'email' : 'E-mail',
            'telefone' : 'Telefone',
            'dataReserva' : 'Data da Reserva',
            'horaReserva' : 'Hora da Reserva',
            'numPessoas' : 'Número de Pessoas',
            'mensagem' : 'mensagem',
        }

        widgets = {
            'nomeCompleto': forms.TextInput(
                attrs={'class':'form-control', 
                       'placeholder' : 'Nome completo',
                       'name' : 'name',
                       'id' : 'name',
                       'required' : ''}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control', 
                       'placeholder' : 'Seu e-mail',
                       'name' : 'email',
                       'id' : 'email',
                       'required' : ''}
            ),
            'telefone': forms.TextInput(
                attrs={'class':'form-control', 
                       'placeholder' : 'Seu Telefone: (00) 90000-0000',
                       'name' : 'phone',
                       'id' : 'phone',
                       'required' : ''}
            ),
            'dataReserva': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class':'form-control', 
                       'type' : 'date',
                       'name' : 'date',
                       'id' : 'date',
                       'required' : ''}
            ),
            'horaReserva': forms.TimeInput(
                attrs={'class':'form-control', 
                       'type' : 'time',
                       'name' : 'time',
                       'id' : 'time',
                       'required' : ''}
            ),
            'numPessoas': forms.NumberInput(
                attrs={'class':'form-control', 
                       'placeholder' : 'Número de Pessoas',
                       'name' : 'people',
                       'id' : 'people',
                       'required' : ''}
            ),
            'mensagem': forms.TextInput(
                attrs={'class':'form-control', 
                       'placeholder' : 'Mensagem (informções adicionais, observações e etc)',
                       'name' : 'message',
                       'id' : 'message',
                       'rows' : '5'}
            )
        }