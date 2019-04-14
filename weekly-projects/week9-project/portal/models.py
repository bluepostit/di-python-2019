from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    rating = models.FloatField()
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    cover_url = models.URLField()
    imdb_id = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({})".format(self.title, self.year)


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

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.text


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
