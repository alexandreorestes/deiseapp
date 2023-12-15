from django.shortcuts import render, redirect
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