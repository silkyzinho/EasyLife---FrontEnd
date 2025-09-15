from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, CadastrarForm
from .models import Usuario, Plano
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404

def home_view(request):
    return render(request, 'home.html')

# usuario

def cadastrar(request):
    if request.method == 'POST':
        form = CadastrarForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            user = User.objects.create_user(username=username, password=password)

            usuario = Usuario.objects.create(user=user, role=role)

            return redirect('') 
    else:
        form = CadastrarForm()
    return render(request, 'cadastrar.html')


@csrf_exempt  #  REMOVER DA PRODUCAO
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Login realizado com sucesso!'})

                messages.success(request, 'Login realizado com sucesso!')
                return redirect('')
    else:
        messages.error(request, 'nome ou senha inválidos.')
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def exibir_usuario(request, id=None):
    usuario = get_object_or_404(Usuario, id=id)
    usuario = {
        "user": Usuario.user,
        "plano": Usuario.plano,
        "picture": Usuario.picture,
    }
    return render(request, 'exibir_usuario.html', usuario)

@login_required
def editar_usuario(request):
    pass

@login_required
def excluir_usuario(request):
    user = request.user

    if request.method == 'POST':
        user.delete()          # apaga o usuário do banco
        logout(request)        # encerra a sessão
        return redirect('')  # volta para tela de login

@login_required
def logout(request):
    logout(request)
    return redirect('home')

# plano

def criar_plano(request):
    pass

def exibir_plano(request):
    pass

def excluir_plano(request):
    pass