from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Conta, Empresa, Servico, Categoria
from django.contrib import messages


# Create your views here.

def criar_conta(request):
    if request.method == 'POST':
        empresa_id = request.POST.get('empresa')
        servico_id = request.POST.get('servico')
        categoria_id = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        tipo = request.POST.get('tipo')
        data_vencimento = request.POST.get('data_vencimento')
        data_pagamento = request.POST.get('data_pagamento')
        resultado = request.POST.get('resultado')

        # Pega os objetos relacionados
        empresa = Empresa.objects.get(id=empresa_id)
        servico = Servico.objects.get(id=servico_id)
        categoria = Categoria.objects.get(id=categoria_id)

        # Cria a conta
        conta = Conta.objects.create(
            usuario=request.user,
            empresa=empresa,
            servico=servico,
            categoria=categoria,
            descricao=descricao,
            valor=valor,
            tipo=tipo,
            data_vencimento=data_vencimento,
            data_pagamento=data_pagamento,
            resultado=resultado
        )
        conta.save()

def exibir_conta(request):
    pass

def excluir_conta(request):
    conta = request.conta

    if request.method == 'POST':
        conta.delete()          # apaga a conta do banco
        return redirect('') 

def calculos(request):
    if request.method == 'POST':
        salario = float(request.POST.get('salario', 0))
        extra = float(request.POST.get('extra', 0))
        salario_total = salario + extra

    total_contas = 0
    for i in Categoria:
        pass

def historico(request):
    return render(request, '')

def comparacao(request):
    return render(request, '')

def criar_categorias(request):
    categorias = (
        "Casa",
        "Alimentação",
        "Saúde e Beleza",
        "Transporte",
        "Educação",
        "Extras",
        "Comparação"
    )
    
    for nome in categorias:
        Categoria.objects.create(
            nome=nome,
            slug=nome
        )

    return render(request, '', {'categorias': categorias})

def servicos(request):
    servicos = Servico.objects.create()
    servicos_por_categoria = {
        "Casa": ["Aluguel", "Agua", "Luz", "Gas", "TV acabo", "Internet", "Telefone", "Servicos/Produtos", "Outros"],
        "Alimentação": ["Mercado", "Fora", "Hort frut", "Feira", "Outros"],
        "Transporte": ["Publico", "Gasolina", "Manutencao", "Seguro", "Táxi"],
        "Saúde e Beleza": ["Farmácia", "Plano", "Exames", "Produtos", "Academia", "Salao", "Outros"],
        "Educação": ["Mensalidade", "Material Escolar", "Cursos", "Outros"],
        "Extras": ["Viagens", "Roupas", "Cinema", "Shows", "Festas", "Presentes", "Animais", "Outros"],
        "Comparação": []
    }

    return render(request, '', {'servicos': servicos})