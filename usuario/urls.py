from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('boas_vindas/',views.boas_vindas, name='boas_vindas'),
    path('loserperfil/', views.loserperfil, name='loserperfil'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('excluir_usuario/', views.excluir_usuario, name='excluir_usuario'),
    path('logout/', views.logout, name='logout'),
    path('criar_plano/', views.criar_plano, name='criar_plano'),
    path('exibir_plano/', views.exibir_plano, name='exibir_plano'),
    path('excluir_plano/', views.excluir_plano, name='excluir_plano'),
]