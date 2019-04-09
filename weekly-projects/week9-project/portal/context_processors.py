from .forms import SearchForm


def nav_search_form(request):
    return {
        'nav_search_form': SearchForm()
    }
