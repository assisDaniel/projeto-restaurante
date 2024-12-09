from django.views.generic import TemplateView
from restaurante.models import Cardapio, Categoria


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categorias'] = Categoria.objects.all()

        context['itens'] = Cardapio.objects.all()
        
        return context
        
