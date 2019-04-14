#!/usr/bin/env python3

import os
import random
import django
from faker import Faker
import imdb


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviews.settings')

django.setup()

from django.contrib.auth.models import User
from portal.models import Movie, MovieReview, MovieReviewComment, MovieReviewVote


def create_users(delete=False):
    if delete:
        User.objects.all().delete()

    users = [
        {
            'first_name': 'Albert',
            'last_name': 'Einstein',
            'password': 'e=mc^2'
        },
        {
            'first_name': 'Marie',
            'last_name': 'Curie',
            'password': 'radioact'
        },
        {
            'first_name': 'Edward',
            'last_name': 'Jenner',
            'password': 'vaccines'
        }
    ]

    for user in users:
        first = user['first_name']
        last = user['last_name']
        username = first[0].lower() \
            + '_' + last.lower()
        email = username + "@science.fake"
        password = user['password']

        user_obj = User.objects.create_user(
            username, email, password)
        user_obj.first_name = first
        user_obj.last_name = last
        user_obj.save()


def create_movies(delete=False):
    if delete:
        Movie.objects.all().delete()

    im = imdb.IMDb()
    movies = im.get_top250_movies()[0:20]
    for movie in movies:
        print('updating %s' % movie['title'])
        im.update(movie, ['main'])
        print('done')
        movie_obj = Movie(
            rating=movie['rating'],
            title=movie['title'],
            year=movie['year'],
            cover_url=movie['full-size cover url'],
            imdb_id=movie.movieID
        )
        movie_obj.save()


def create_reviews(delete=False):
    if delete:
        MovieReview.objects.all().delete()

    users = User.objects.all()

    faker = Faker()
    for movie in Movie.objects.all():
        user = random.choice(users)
        rating = random.randint(1, 10)

        review = MovieReview(
            movie=movie,
            title=faker.sentence(),
            text=faker.paragraph(),
            rating=rating,
            user=user)
        review.save()


def create_comments(delete=False):
    if delete:
        MovieReviewComment.objects.all().delete()

    faker = Faker()
    for review in MovieReview.objects.all():
        for user in User.objects.all():
            if review.user == user:
                continue

            text = faker.sentence()
            title = ' '.join(text.split()[0:2])

            comment = MovieReviewComment(
                movie_review=review,
                title=title,
                text=text,
                user=user)
            comment.save()


def create_votes(delete=False):
    if delete:
        MovieReviewVote.objects.all().delete()

    for review in MovieReview.objects.all():
        for user in User.objects.all():
            if review.user == user:
                continue

            value = random.choice(('u', 'd'))

            vote = MovieReviewVote(
                value=value,
                movie_review=review,
                user=user)
            vote.save()


create_users(True)
create_movies(True)
create_reviews(True)
create_comments(True)
create_votes(True)
