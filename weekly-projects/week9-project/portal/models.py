from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    '''To do: implement this model'''


class MovieReview(models.Model):

    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )

    # To do: add the relevant fields.


class MovieReviewVote(models.Model):

    VOTE_CHOICES = (
        ('u', 'Up'),
        ('d', 'Down')
    )

    movie_review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
    value = models.CharField(max_length=1, choices=VOTE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MovieReviewComment(models.Model):
    movie_review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
