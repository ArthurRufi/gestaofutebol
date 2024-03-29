from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
#esse app deve ser apagado


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "teste/html/index.html", context, status= 404)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "teste/html/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def pagnull(request, null):
    #o null vai ser usado no html para fins finais kkkkkkkk
    context = {'null': null}
    return HttpResponse("Ta procurando demais %s nao existe" %null)