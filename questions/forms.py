from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'correct_answer']
        widgets = {
            'question_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your question here'
            }),
            'correct_answer': forms.RadioSelect(choices=[
                (True, 'True'),
                (False, 'False')
            ])
        }
