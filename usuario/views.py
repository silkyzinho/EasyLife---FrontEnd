from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
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

            user = User.objects.create_user(username=username, password=password)
            Usuario.objects.create(user=user)
            
            auth_login(request, user)
            
            messages.success(request, f'Usuário {username} cadastrado com sucesso!')
            return redirect('exibir_usuario')
    else:
        form = CadastrarForm()

    return render(request, 'cadastrar.html', {'form': form})

@csrf_exempt  #  REMOVER DA PRODUCAO
def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)

                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Login realizado com sucesso!'})

                messages.success(request, 'Login realizado com sucesso!')
                return redirect('exibir_usuario')
            else:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'message': 'Nome ou senha inválidos.'})

                messages.error(request, 'Nome ou senha inválidos.')

        else:
            form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def boas_vindas(request):
    return render(request, 'boas_vindas.html')

@login_required
def loserperfil(request, id=None):
    usuario = get_object_or_404(Usuario, user=request.user)
    return render(request, 'loserperfil.html', {'usuario': usuario})

@login_required
def editar_usuario(request):
    pass

@login_required
def excluir_usuario(request):
    user = request.user

    if request.method == 'POST':
        user.delete()
        auth_logout(request)
        return redirect('login.html')
    return render(request, '') 

@login_required
def logout(request):
    auth_logout(request)        # encerra a sessão
    return redirect('home.html')

# plano

@login_required
def criar_plano(request):
    pass

@login_required
def exibir_plano(request):
    pass

@login_required
def excluir_plano(request):
    pass