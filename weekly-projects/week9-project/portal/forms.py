from django import forms
from django.forms import ModelForm, TextInput

from .models import MovieReviewComment as Comment, MovieReview


class SearchForm(forms.Form):
    search_text = forms.CharField(
        label='Search',
        max_length=100,
        widget=TextInput(attrs={
            'class': "form-control mr-sm-2",
            'type': "search"
        })
    )


class MovieReviewForm(ModelForm):
    class Meta:
        model = MovieReview
        fields = ['movie', 'title', 'text', 'rating']
        widgets = {'movie': forms.HiddenInput}


class MovieReviewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('movie_review', 'title', 'text')
        widgets = {'movie_review': forms.HiddenInput}
