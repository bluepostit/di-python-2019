from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=100)
    publication_date = forms.DateTimeField()
