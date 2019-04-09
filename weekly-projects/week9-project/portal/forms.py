from django import forms
from django.forms import TextInput


class SearchForm(forms.Form):
    search_text = forms.CharField(
        label='Search',
        max_length=100,
        widget=TextInput(attrs={
            'class': "form-control mr-sm-2",
            'type': "search"
        })
    )
