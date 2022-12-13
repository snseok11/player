from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Question, Choice
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
def index(request) :
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #1 output = ', '.join([q.question_text for q in latest_question_list])
    #2 template = loader.get_template('polls/index.html')
    context = {
         'latest_question_list' : latest_question_list
    }
    #2 return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)
def detail(request, question_id) :
    #1 return HttpResponse("you're looking for detail %s" % question_id)
    #2 try :
    #2     question = Question.objects.get(pk=question_id)
    #2 except Question.DoesNotExist:
    #2     raise Http404("Question does not exist")
    #2 return render(request, "polls/detail.html", {'question' : question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question' : question})

def results(request, question_id) :
    # response = "you're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id) :
    # return HttpResponse("you're voting on question %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try :
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question' : question, 'error_message' : "you didn't select a choice.",})
    else :
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))