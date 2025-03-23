from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')


def sobre(request):
    return render(request, 'core/sobre.html')

def projetos(request):
    return render(request, 'core/projetos.html')

def blog(request):
    return render(request, 'core/blog.html')

def conteudo(request):
    return render(request, 'core/conteudo.html')
