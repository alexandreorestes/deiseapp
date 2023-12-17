from django.shortcuts import render, redirect
from django.db.models import Sum  # Importe Sum do Django
from .forms import VendaForm
from .models import Venda

def inserir_dados(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Página de sucesso após inserção
    else:
        form = VendaForm()
    
    return render(request, 'inserir_dados.html', {'form': form})

def pagina_de_sucesso(request):
    return render(request, 'pagina_de_sucesso.html')  # Renderizando a página de sucesso

def home(request):
    return render(request, 'home.html')

def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'listar_vendas.html', {'vendas': vendas})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Venda
from .forms import VendaForm

def editar_venda(request, venda_id):
    # Busca a venda correspondente ao ID ou retorna um erro 404 se não encontrada
    venda = get_object_or_404(Venda, pk=venda_id)

    if request.method == 'POST':
        # Se for uma requisição POST, cria um formulário com os dados atualizados
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('listar_vendas')  # Redireciona para a lista de vendas após editar
    else:
        # Se for uma requisição GET, cria um formulário pré-preenchido com os detalhes da venda
        form = VendaForm(instance=venda)
    
    return render(request, 'editar_venda.html', {'form': form})

def confirmar_exclusao(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)
    return render(request, 'confirmar_exclusao.html', {'venda': venda})

def excluir_venda(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)
    venda.delete()
    return redirect('listar_vendas')


def listar_vendas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')

    vendas = Venda.objects.all()

    # Filtra as vendas por intervalo de datas, se fornecido
    if data_inicial and data_final:
        vendas = vendas.filter(data__range=[data_inicial, data_final])

    # Calcula a soma dos valores das vendas filtradas
    soma_valores = vendas.aggregate(soma_valores=Sum('valor'))['soma_valores']

    return render(request, 'listar_vendas.html', {'vendas': vendas, 'soma_valores': soma_valores})
