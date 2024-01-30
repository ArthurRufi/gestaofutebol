from django.shortcuts import render, redirect
from django.http import HttpResponse
from utils.scriptsmain import playersfunc
import os
from django.core.paginator import Paginator

def main(request):
    return render(request, 'main/html/index.html')


def login(request):
    return HttpResponse("yor reuqest %s" %request)


def pagnull(request, null):
    #o null vai ser usado no html para fins finais kkkkkkkk
    context = {'null': null}
    return HttpResponse("Ta procurando demais, %s nao existe" %null)


def mainteste(request):
    # Caminho para o diretório de imagens
    diretorio_imagens = os.path.join('main', 'static', 'main', 'images', 'papapa')

    # Lista de nomes de arquivo no diretório
    imagens = os.listdir(diretorio_imagens)

    # Paginação
    paginator = Paginator(imagens, 9)
    page = request.GET.get('page', 1)
    imagens_pagina = paginator.get_page(page)

    return render(request, 'main/html/alma.html', {'imagens': imagens_pagina})


def linkimagem(request):
    nome_da_imagem = request.GET.get('imagem', None)

    if nome_da_imagem:
        # Lógica para determinar o destino do redirecionamento com base no nome_da_imagem
        # Exemplo: se a imagem for 'imagem1.jpg', redirecione para https://www.example.com/imagem1
        destino = f'https://www.example.com/{nome_da_imagem.replace(".jpg", "")}'
        return redirect(destino)
    else:
        # Lógica padrão se nenhum nome de imagem for fornecido
        return render(request, 'main/html/index.html')