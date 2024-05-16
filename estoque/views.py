from django.shortcuts import render
from estoque.forms import ProdutoModelForm
from estoque.models import Produto
from django.views import View
from django.views.generic import ListView, CreateView, DetailView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class HomeView(View):

    def get(self, request):
        return render(
            request,
            'home.html',
        )

@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutosView(ListView):
    model = Produto
    template_name = 'estoque.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        produto = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')

        if search:
            produto = produto.filter(nome__icontains=search)
        return produto

@method_decorator(login_required(login_url='login'), name='dispatch')
class AdicionarProdutoView(CreateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'add_produto.html'
    success_url = '/produtos/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'profile'


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_update.html'
    form_class = ProdutoModelForm

    def get_success_url(self):
        return reverse_lazy('produto_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_delete.html'
    success_url = '/home/'