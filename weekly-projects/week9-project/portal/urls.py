from django.urls import path

from . import views

app_name = 'portal'
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<movie_id>/', views.show_movie, name='show_movie'),
    path('reviews/<int:review_id>/', views.show_review, name='show_review'),
    path('reviews/search/', views.search_reviews, name='search_reviews'),
    path('reviews/add/<int:movie_id>/', views.add_review, name='add_review'),
    path('comments/add/', views.add_comment, name='add_comment'),
]