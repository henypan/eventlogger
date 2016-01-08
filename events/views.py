from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question
from .forms import InformationForm
from .lucene import start_index


class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'question_list'
    
    def get_queryset(self):
        return Question.objects.all().order_by('number')[:200]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'events/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'events/results.html'


def convert_difficulty(difficulty):
    difficulty = difficulty.lower()
    if len(difficulty) >= 1:
        if difficulty[0] == 'e':
            difficulty = 'Easy'
        elif difficulty[0] == 'm':
            difficulty = 'Medium'
        elif difficulty[0] == 'h':
            difficulty = 'Hard'
    return difficulty


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            p.question_text = p.question_text.lower()
            p.method = form.cleaned_data.get('method', '')
            p.note = form.cleaned_data.get('note', '')
            p.pub_date = timezone.now()
            p.difficulty = convert_difficulty(p.difficulty)
            p.frequencies = start_index('index.json', p)
            p.save()
    return HttpResponseRedirect(reverse('events:results', args=(p.id,)))
