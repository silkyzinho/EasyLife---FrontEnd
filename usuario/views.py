from django.shortcuts import render, redirect
from django.contrib import messages  #framework de mensagens
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout

def home_view(request):
    return render(request, 'home.html')

# usuario

def cadastrar(request):
    if request.method == 'POST':  # se o usuário enviou o formulário
        username = request.POST.get('username')
        picture = request.POST.get('picture')
        salario = request.POST.get('salario')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:          # se as duas senhas sao diferentes
            messages.error(request, "As senhas não conferem.")
        else:            # Cria o novo usuário no banco de dados
            user = User.objects.create_user(username=username, picture=picture, salario=salario, password=password1)
            usuario = Usuario.objects.create(user=user)
            user.save()

def login(request):
    return render(request, 'login.html')

def exibir_usuario(request):
    
    return render(request, 'exibir.html')

def editar_usuario(request):
    pass

def excluir_usuario(request):
    return redirect('usuario_login')

def logout(request):
    logout()
    return redirect('usuario_login')

# plano

def criar_plano(request):
    return render(request, 'criar_plano')

def exibir_plano(request):
    return render(request, 'exibir_plano')

def excluir_plano(request):
    return redirect('criar_plano')