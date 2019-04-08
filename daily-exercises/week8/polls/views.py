from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Choice, Question
from .forms import QuestionForm


def add_to_question_history(session, question):
    viewed_questions = session.get('viewed_questions', [])
    viewed_questions = set(viewed_questions)
    viewed_questions.add(question.pk)
    session['viewed_questions'] = list(viewed_questions)


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

    # this variable can have any name...
    raptor = {
        'question': q,
        'choices': choices
    }
    # add to session
    add_to_question_history(request.session, q)
    # debug:
    print(request.session['viewed_questions'])
    return render(request, 'polls/show-question.html', raptor)


def vote(request, question_id, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    choice.votes += 1
    choice.save()

    return redirect('polls:show_dinosaur', question_id=question_id)


def add_question(request):
    # any name will do (but 'form' would be best)
    f = QuestionForm()
    if request.method == 'POST':
        f = QuestionForm(request.POST)
        if f.is_valid():
            question = f.save()
            return redirect('polls:show_dinosaur',
                            question_id=question.pk)

    context = {
        'form': f
    }
    return render(request, 'polls/add-question.html', context)
