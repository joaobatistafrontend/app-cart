from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import Produto
from django.urls import reverse_lazy



class CriarProduto(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    template_name = 'crud/creat.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('home')
    group_required = u'adm'

class ListaProduto(LoginRequiredMixin,ListView):
    template_name = 'crud/list.html'
    model = Produto
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['produtos'] = Produto.objects.all()
        return context

class EditarProduto(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    template_name = 'crud/update.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('list')
    group_required = u'adm'


class DeletarProduto(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    template_name = 'crud/delete.html'
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('list')
    group_required = u'adm'
