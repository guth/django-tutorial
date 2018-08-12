from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('date_published')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ', '.join([q.text for q in latest_question_list])
    # return HttpResponse(output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    # try:
    #     # Alternatively: id=question_id
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    # return HttpResponse("You're looking at question %s." % question_id)

    # There’s also a get_list_or_404() function, which works just
    # as get_object_or_404() – except using filter() instead of get().
    # It raises Http404 if the list is empty.
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)