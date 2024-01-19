from django.shortcuts import render
from django.http import HttpResponse



def main(request):
    return render(request, 'main/html/index.html')


def login(request):
    return HttpResponse("yor reuqest %s" %request)


def pagnull(request, null):
    #o null vai ser usado no html para fins finais kkkkkkkk
    context = {'null': null}
    return HttpResponse("Ta procurando demais, %s nao existe" %null)