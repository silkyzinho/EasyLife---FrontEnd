from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('boas_vindas/', views.boas_vindas, name='boas_vindas'),
    path('exibir_perfil/', views.exibir_perfil, name='exibir_perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('remover_foto/', views.remover_foto, name='remover_foto'),
    path('alterar_foto/', views.alterar_foto, name='alterar_foto'),
    path('excluir_usuario/', views.excluir_usuario, name='excluir_usuario'),
    path('logout/', views.logout, name='logout'),
    path('criar_plano/', views.criar_plano, name='criar_plano'),
    path('exibir_plano/', views.exibir_plano, name='exibir_plano'),
    path('cancelar_plano/', views.cancelar_plano, name='cancelar_plano'),
]