from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request, 'polls/index.html',context)
    #render shortcut: takes request, template, dict (mapping template var
    # to python var)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse(f"You're looking at the result of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
    

# Create your views here.
