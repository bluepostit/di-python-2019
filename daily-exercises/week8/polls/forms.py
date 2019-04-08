from django import forms
from django.forms.widgets import SelectDateWidget

from .models import Question


class QuestionForm(forms.ModelForm):
    pub_date = forms.DateField(widget=SelectDateWidget)

    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
