from django.shortcuts import render


def info_page(request):
    return render(request, 'visitors/info.html')
