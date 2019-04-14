from django.db.models import Q

from .models import MovieReview as Review


def search_reviews_with_text(text):
    results = Review.objects.filter(
        Q(title__icontains=text) |
        Q(text__icontains=text) |
        Q(user__first_name__icontains=text) |
        Q(user__last_name__icontains=text) |
        Q(movie__title__icontains=text) |
        Q(movie__pk__icontains=text))
    return results
