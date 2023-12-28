from django.shortcuts import render
from django.http import HttpResponse



def main(request):
    return render(request, 'main/html/index.html')


def details(request, questionid):
    return HttpResponse("You are looking at question %s" % questionid)

def results(request, questionid):
    response = " You are looking results of question %s."
    return HttpResponse(response % questionid)


def vote(request, questionid):
    return HttpResponse("You voting on questions %s" % questionid)


def login(request):
    return HttpResponse("yor reuqest %s" %request)


def pagnull(request, null):
    #o null vai ser usado no html para fins finais kkkkkkkk
    context = {'null': null}
    return HttpResponse("Ta procurando demais %s nao existe" %null)