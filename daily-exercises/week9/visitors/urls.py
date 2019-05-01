from django.urls import path

from . import views


app_name = 'visitors'
urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info_page, name='info'),
    path('vacancies/', views.show_vacancies, name='vacancies'),
    path('booking/', views.make_booking, name='make_booking'),
]
