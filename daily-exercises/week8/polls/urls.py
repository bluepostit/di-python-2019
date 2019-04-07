from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
    path('questions/', views.show_questions, name='show_questions'),
    path('questions/<int:question_id>/', views.show_question,
        name='show_dinosaur'),
    path('questions/<int:question_id>/vote/<int:choice_id>',
    views.vote, name='vote'),
    path('questions/add/', views.add_question, name='add_question'),
]