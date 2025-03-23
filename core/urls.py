from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('projetos/', views.projetos, name='projetos'),
    path('blog/', views.blog, name='blog'),
    path('conteudo/', views.conteudo, name='conteudo'),
]
