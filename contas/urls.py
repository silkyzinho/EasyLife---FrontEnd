from django.urls import path
from . import views

urlpatterns = [
    path('criar_conta/', views.criar_conta, name='criar_conta'),
    path('exibir_conta/', views.exibir_conta, name='exibir_conta'),
    path('excluir_conta/', views.excluir_conta, name='excluir_conta'),
    path('calculos/', views.calculos, name='calculos'),
    path('historico/', views.historico, name='historico'),
    path('comparacao/', views.comparacao, name='comparacao'),
    path('criar_categorias/', views.criar_categorias, name='criar_categorias'),
    path('servicos/', views.servicos, name='servicos'),
]