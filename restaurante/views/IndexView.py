from django.views.generic import TemplateView, CreateView
from restaurante.models import Cardapio, Categoria, Reserva
from restaurante.forms import ReservasForm


class IndexTemplateView(CreateView):
    template_name = 'index.html'
    model = Reserva
    form_class = ReservasForm
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['itens'] = Cardapio.objects.all()
        
        return context
    
    def form_valid(self, form):
        return super().form_valid(form)
