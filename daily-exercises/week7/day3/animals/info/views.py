from django.shortcuts import render

from .models import Animal, Family


def index(request):
	return render(request, 'info/index.html')


def show_family(request, family_id):
	family = Family.objects.get(pk=family_id)
	return render(request, 'info/show_family.html', {
		'family': family})


def show_animals(request):
	animals = Animal.objects.all()
	context = {
		'animals': animals
	}
	return render(request, 'info/show_animals.html', context)


# def show_animal(request, animal_id):
# 	return render(request, 'info/show_animal.html')
