from django.urls import path

from . import views


app_name = 'visitors'
urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info_page, name='info'),
    path('vacancies/', views.show_vacancies, name='show_vacancies'),
]
