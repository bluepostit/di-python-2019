from django.urls import path

from . import views


app_name = 'visitors'
urlpatterns = [
    path('', views.info_page, name='info'),
]
