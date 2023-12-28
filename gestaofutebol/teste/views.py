from django.shortcuts import render
from django.http import HttpResponse
#esse app deve ser apagado


def index (request):
    return render(request, 'teste/html/index.html')