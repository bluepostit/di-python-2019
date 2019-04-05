from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .models import Person, PersonStatus

def index(request):
	return render(request, 'portal/index.html')


def add_person(request):
    if request.method == 'POST':
        post = request.POST
        first_name = post['first_name']
        last_name = post['last_name']
        other_name = post['other_name']
        status_text = post['status']
        id_number = post['id_number']
        mobile = post['mobile']
        email = post['email']
        description = post['description']
        # Dangerous!
        status = PersonStatus.objects.get(
            name__exact=status_text)

        person = Person(
            first_name=first_name,
            last_name=last_name,
            other_name=other_name,
            status=status,
            id_number=id_number,
            mobile=mobile,
            email=email,
            description=description)
        person.save()
        return redirect('portal:index')
    return render(request, 'portal/add_person.html')


def show_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'portal/show_person.html', {
        'person': person })


def show_safe_persons(request):
    persons = Person.objects.filter(status__name='safe')
    return render(request, 'portal/show_persons.html', {
        'title': 'Persons marked as Safe',
        'main_heading': 'Persons Marked as Safe',
        'persons': persons })


def search_person(request):
    context = None
    if request.method != 'POST':
        return redirect('portal:index')

    text = request.POST.get('search', '')
    results = Person.objects.filter(
        Q(first_name__icontains=text) |
        Q(last_name__icontains=text) |
        Q(other_name__icontains=text) |
        Q(description__icontains=text))

    heading = 'Person Search:'
    context = {
        'main_heading': heading,
        'heading_subtext': '"{}"'.format(text),
        'title': heading,
        'search_text': text,
        'persons': results
    }
    return render(request, 'portal/show_persons.html', context)
