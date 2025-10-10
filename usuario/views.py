from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import LoginForm, CadastrarForm
from .models import Usuario, Plano
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test

def home_view(request):
    return render(request, 'home.html')

# usuario 

def cadastrar(request):
    if request.method == 'POST':
        form = CadastrarForm(request.POST)
        if form.is_valid():
            # Extrai o nome de usuário e a senha do formulário.
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            picture = form.cleaned_data.get('picture')


            user = User.objects.create_user(username=username, email=email, password=password)
            Usuario.objects.create(user=user, picture=picture)  
            auth_login(request, user)
            
            messages.success(request, f'Usuário {username} cadastrado com sucesso!')
            return redirect('boas_vindas')
    else:
        form = CadastrarForm()

    return render(request, 'cadastrar.html', {'form': form})

def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('boas_vindas')
            
            else:
                messages.error(request, 'Nome ou senha inválidos.')

    return render(request, 'login.html', {'form': form})

@login_required
def boas_vindas(request):
    return render(request, 'boas_vindas.html')

@login_required
def exibir_perfil(request, id=None):
    # Busca o perfil do usuário
    usuario = Usuario()
    user = User()
    plano = Plano()
    usuario.user = user
    usuario.user.username = "Gustavo Ferreira"
    usuario.plano = plano
    usuario.plano.nome = "Gratuito"

    return render(request, 'exibir_perfil.html', {'usuario': usuario})

@login_required
def editar_usuario(request):
    pass

@login_required
def excluir_usuario(request):
    user = request.user

    if request.method == 'POST':
        user.delete()    #exclui
        auth_logout(request)    #logout
        return redirect('login')
    return render(request, '') 

@login_required
def logout(request):
    auth_logout(request)        # encerra a sessão
    return redirect('home')

# plano

@login_required
def criar_plano(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        valor = request.POST.get("valor")
        prazo = request.POST.get("prazo")

        plano = Plano.objects.create(
            nome=nome,
            valor=valor,
            prazo=prazo,                
            )
        
        if hasattr(request.user, "perfil"):
            request.user.perfil.plano = plano
            request.user.perfil.save()

        return redirect('exibir_perfil')  

    return render(request, '')

def is_usuario_plano(user):
    return hasattr(user, 'perfil') and user.perfil.plano is not None

@user_passes_test(is_usuario_plano)
@login_required
def exibir_plano(request):
    planos = Plano.objects.all()
    return render(request, '', {'planos': planos})

@user_passes_test(is_usuario_plano)
@login_required
def excluir_plano(request):
    plano = get_object_or_404(Plano)
    if request.method == 'POST':
        plano.delete()
        messages.success(request, 'Plano excluído com sucesso!')
        return redirect('')
    return render(request, '', {'plano': plano})