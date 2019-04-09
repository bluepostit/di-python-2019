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
    movies = im.get_top250_movies()[0:10]
    for movie in movies:
        print('updating %s' % movie['title'])
        im.update(movie, ['main'])
        print('done')
        # To do: use the data in `movie` to populate a
        # new Movie object, then save it.


def create_reviews(delete=False):
    if delete:
        MovieReview.objects.all().delete()

    # To do: create at least one review for each movie.


def create_comments(delete=False):
    if delete:
        MovieReviewComment.objects.all().delete()

    # To do: create movie comments


def create_votes(delete=False):
    if delete:
        MovieReviewVote.objects.all().delete()

    # To do: create movie votes (up/down)


create_users(True)
create_movies(True)
create_reviews(True)
# create_comments(True)
# create_votes(True)
