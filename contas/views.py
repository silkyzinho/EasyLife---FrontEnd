from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Conta, Empresa, Servico, Categoria
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

CATEGORIAS_CALCULO = {
    'casa': ['aluguel', 'agua', 'luz', 'gas', 'internet', 'telefone', 'servicos_prestacoes', 'outros_casa'],
    'alimentacao': ['mercado', 'fora', 'hort_frut', 'feira', 'outros_alimentacao'],
    'transporte': ['publico', 'gasolina', 'manutencao', 'seguro', 'taxi', 'outros_transporte'],
    'saude_e_beleza': ['farmacia', 'plano', 'exames', 'produtos', 'academia', 'salao', 'outros_saude_e_beleza'],
    'educacao': ['mensalidade', 'material_escolar', 'cursos', 'outros_educacao'],
    'extras': ['viagens', 'roupas', 'cinema', 'shows', 'festas', 'presentes', 'animais', 'outros_extras'],
    'comparacao': []
}

@login_required
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

@login_required
def exibir_conta(request):
    pass

@login_required
def excluir_conta(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id, usuario=request.user)
    if request.method == 'POST':
        conta.delete()          # Apaga a conta do banco.
        messages.success(request, "Conta excluída com sucesso!")
        return redirect('')

    if request.method == 'POST':
        conta.delete()          # apaga a conta do banco
        return redirect('') 

@login_required
def calculos(request):
    context = {}
    if request.method == 'POST':
        def get_float(field_name):
            return float(request.POST.get(field_name) or 0)
        # Salario
        salario = get_float('salario')
        extra = get_float('extra')
        salario_total = salario + extra
        context.update({
            'salario': salario,
            'extra': extra,
            'salario_total': salario_total,
        })
        
        total_despesas = 0
        
        # Itera sobre o dicionário padronizado para calcular os totais
        for categoria_nome, fields in CATEGORIAS_CALCULO.items():
            total_categoria = 0
            for field in fields:
                value = get_float(field)
                context[field] = value
                total_categoria += value
            
            # Adiciona o total da categoria ao contexto (ex: context['total_casa'] = 500)
            context[f'total_{categoria_nome}'] = total_categoria
            total_despesas += total_categoria
        resultado = salario_total - total_despesas
        context['total_despesas'] = total_despesas
        context['resultado'] = resultado
    return render(request, 'calculos.html', context)

@login_required
def historico(request):
    return render(request, 'historico.html')

@login_required
def comparacao(request):
    return render(request, 'comparar.html')

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
    servicos_categoria = {
      "Casa": ["Aluguel", "Agua", "Luz", "Gas", "TV acabo", "Internet", "Telefone", "Servicos/Produtos", "Outros"],
      "Alimentação": ["Mercado", "Fora", "Hort frut", "Feira", "Outros"], 
      "Transporte": ["Publico", "Gasolina", "Manutencao", "Seguro", "Táxi"], 
      "Saúde e Beleza": ["Farmácia", "Plano", "Exames", "Produtos", "Academia", "Salao", "Outros"],
      "Educação": ["Mensalidade", "Material Escolar", "Cursos", "Outros"],
      "Extras": ["Viagens", "Roupas", "Cinema", "Shows", "Festas", "Presentes", "Animais", "Outros"], 
      "Comparação": [] 
    }

    return render(request, '', {'servicos': servicos})