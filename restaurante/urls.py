from django.urls import path
 
from restaurante.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='home'),
]