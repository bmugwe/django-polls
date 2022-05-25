from asyncore import poll
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, Http404
from django.template import loader

from polls.models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "you're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})

def detail_1(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
