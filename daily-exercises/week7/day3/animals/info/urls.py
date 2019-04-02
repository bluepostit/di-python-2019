from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('family/<int:family_id>/', views.show_family, name='show_family'),
	path('animal/', views.show_animals, name='show_animals')
	# path('animal/<int:animal_id>/', views.show_animal, name='show_animal'),
]