from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
	path('', views.index, name='index'),
	path('persons/add/', views.add_person, name='add_person'),
    path('persons/<int:person_id>/', views.show_person, name='show_person'),
    path('persons/search/', views.search_person, name='search_person'),
    path('persons/show_safe/', views.show_safe_persons, name='show_safe_persons'),
]