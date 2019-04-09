# ... other imports...

# You might find some useful functions here...
from . import util


def index(request):
    '''Show a list of all movies. Click on a movie to view it'''


def show_movie(request, movie_id):
    '''Show the given movie, or raise a 404 error'''


def show_review(request, review_id):
    '''Show the given review, or raise a 404 error'''


def search_reviews(request):
    '''Search for reviews using POST data.
    Use a Form object to handle the form and its input.
    If the form does not validate, redirec to the index page.'''


# uncomment this line - find the correct import for it!
# @login_required
def add_review(request, movie_id):
    '''Add a new MovieReview object for the given Movie.
    GET: display the page with an empty form.
    POST: validate the form. If valid, save the form.
          (Add the User to the MovieReview after you call save(False).
          Then call save() with no arguments.)
          If not valid, render the invalid form.
          Be sure to validate the movie as well.'''
