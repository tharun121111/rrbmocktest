# mocktest/forms.py

from django import forms
from .models import UserAnswer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = UserAnswer
        fields = ['answer']
# mocktest/forms.py

from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_answer', 'category']
