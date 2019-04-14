from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Movie, MovieReview
from .forms import MovieReviewCommentForm as CommentForm, \
    MovieReviewForm as ReviewForm, SearchForm
from . import util


def index(request):
    movies = Movie.objects.all()
    return render(request, 'portal/index.html', {'movies': movies})


def show_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'portal/show_movie.html', context)


def show_review(request, review_id):
    review = get_object_or_404(MovieReview, pk=review_id)
    comment_form = CommentForm(initial={
        'movie_review': review
        })
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'portal/show_review.html', context)


def search_reviews(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['search_text']
            reviews = util.search_reviews_with_text(search_text)

            heading = 'Review Search:'
            context = {
                'main_heading': heading,
                'heading_subtext': '"{}"'.format(search_text),
                'title': heading,
                'search_text': search_text,
                'reviews': reviews
            }
            return render(request, 'portal/show_reviews.html', context)
    return redirect('portal:index')


@login_required
def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = ReviewForm(initial={
        'movie': movie
        })

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(False)
            review.user = request.user
            review.save()
            return redirect('portal:show_review', review.pk)

    context = {
        'form': form,
        'movie': movie
    }
    return render(request, 'portal/add_review.html', context)


@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(False)
            comment.user = request.user
            comment.save()
            return redirect('portal:show_review',
                            comment.movie_review.pk)
        print(form.errors)

    return redirect('portal:index')
