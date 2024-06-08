from django.shortcuts import render
from estoque.forms import ProdutoModelForm, FeedbackForm
from estoque.models import Produto, Feedback
from django.views import View
from django.views.generic import ListView, CreateView, DetailView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# View que renderiza a pagina home do projeto
class HomeView(View):

    def get(self, request):
        return render(
            request,
            'home.html',
        )

# Decorator que impeça que quem não esteja logado acesse outras áreas do projeto sem estar logado.
# View que retorna a exibição dos produtos, filtra e ordena pelo nome, além da lógica de busca dos produtos.
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        produto = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')

        if search:
            produto = produto.filter(nome__icontains=search)
        return produto
    
    


# Decorator que impeça que quem não esteja logado acesse outras áreas do projeto sem estar logado.
# View que cuida do cadastro de novos produtos e renderiza a pagina de cadastro de produtos.
@method_decorator(login_required(login_url='login'), name='dispatch')
class AdicionarProdutoView(CreateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'add_produto.html'
    success_url = '/produtos/'

# Decorator que impeça que quem não esteja logado acesse outras áreas do projeto sem estar logado.
# View que cuida de renderizar a página de detalhes do produto.
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'profile'


# Decorator que impeça que quem não esteja logado acesse outras áreas do projeto sem estar logado.
# View que cuida do update de produtos cadastrados e renderiza a página de update dos produtos.
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produto_update.html'
    form_class = ProdutoModelForm

    def get_success_url(self):
        return reverse_lazy('produto_detail', kwargs={'pk': self.object.pk})


# Decorator que impeça que quem não esteja logado acesse outras áreas do projeto sem estar logado.
# View que cuida do delete dos produtos cadastrados e renderiza a página de deleção dos produtos.
@method_decorator(login_required(login_url='login'), name='dispatch')
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_delete.html'
    success_url = '/produtos/'


# Decorator que impeça que quem não esteja logado acesse outras áreas do projeto sem estar logado.
# View que cuida da busca e filtragem de feedbacks do site
@method_decorator(login_required(login_url='login'), name='dispatch')
class FeedbackView(ListView):
    model = Feedback
    template_name = 'feedback.html'
    context_object_name = 'feedbacks'

    def get_queryset(self):
        feedback = super().get_queryset().order_by('-data_feedback')
        search = self.request.GET.get('search')

        if search:
            feedback = feedback.filter(nome__icontains=search)  
        return feedback


@method_decorator(login_required(login_url='login'), name='dispatch')
class AdicionarFeedback(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'add_feedback.html'
    success_url = '/feedback/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback_detail.html'
    context_object_name = 'detail_feedback'

