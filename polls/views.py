from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone
from .models import Question, Choice

class IndexView(generic.ListView):
  # first version
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  # context = {
  #   'latest_question_list':latest_question_list,
  # }
  # change to below
    template_name = 'polls/index.html'
  # order by?
    context_object_name = 'latest_question_list'
  # output = ', '.join([q.question_text for q in latest_question_list])
  # return HttpResponse(template.render(context,request))
    def get_queryset(self):
      """
      Return the last five published questions (not including those set to be published in the future)
      """
      return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
  # try:
  #   question = Question.objects.get(pk = question_id)
  # except Question.DoesNotExist:
  #   raise Http404('Question does not exist')
  # question = get_object_or_404(Question, pk=question_id)
  model = Question
  template_name = 'polls/detail.html'
  # return render(request, 'polls/detail.html', {'question':question})
  def get_queryset(self):
      return Question.objects.filter(pub_date__lte = timezone.now())

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'
  # question = get_object_or_404(Question, pk=question_id)
  # return render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
  question = get_object_or_404(Question,pk=question_id)
  try:
    # request.POST['choice'] returns the ID of the selected choice
    # request.POST['choice'] will raise KeyError if choice wasn't provided in POST data
    selected_choice = question.choice_set.get(pk = request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html',{
      'question':question,
      'error_message':"You didn't select a choice.",
    })
  else:
    selected_choice.votes +=1
    selected_choice.save()
    # alwyas return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the back button
    # reverse() function helps avoid having to hardcode a URL
  return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
