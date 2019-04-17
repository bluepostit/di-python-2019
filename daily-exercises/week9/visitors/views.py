from django.shortcuts import render


def info_page(request):
    return render(request, 'visitors/info.html')


def index(request):
    return render(request, 'visitors/info.html')


def show_vacancies(request):
    return None
