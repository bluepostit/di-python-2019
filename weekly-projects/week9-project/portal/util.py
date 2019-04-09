from django.db.models import Q
from django.http import Http404

from .models import Movie, MovieReview as Review


def search_reviews_with_text(text):
    results = Review.objects.filter(
        Q(title__icontains=text) |
        Q(text__icontains=text) |
        Q(user__first_name__icontains=text) |
        Q(user__last_name__icontains=text) |
        Q(movie__title__icontains=text) |
        Q(movie__pk__icontains=text))
    return results


def get_movie_or_404(movie_id):
    try:
        movie = Movie.objects.get(imdb_id=movie_id)
        return movie
    except:
        print("An error occured retrieving the movie with IMDB ID %s" % movie_id)
        raise Http404("Movie not found")
