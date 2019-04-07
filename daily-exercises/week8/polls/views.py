from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Choice, Question
from .forms import QuestionForm


def index(request):
	return HttpResponse('Hi there')


def show_questions(request):
    context = {
        'questions': Question.objects.all().order_by('question_text')
    }
    return render(request, 'polls/show-questions.html', context)


def show_question(request, question_id):
    # q = Question.objects.get(pk=question_id)
    q = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=q).order_by('choice_text')
    raptor = {
        'question': q,
        'choices': choices
    }
    return render(request, 'polls/show-question.html', raptor)


def vote(request, question_id, choice_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.votes += 1
    choice.save()

    return redirect('polls:show_dinosaur', question_id=question_id)


def add_question(request):
    f = QuestionForm()
    if request.method == 'POST':
        f = QuestionForm(request.POST)
        if f.is_valid():
            question_text = f.cleaned_data['question_text']
            publication_date = f.cleaned_data['publication_date']
            question = Question(
                question_text=question_text,
                pub_date=publication_date)
            question.save()
            return redirect('polls:show_dinosaur',
                question_id=question.pk)

    context = {
        'form': f
    }
    return render(request, 'polls/add-question.html', context)