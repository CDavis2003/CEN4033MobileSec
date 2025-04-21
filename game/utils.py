import random
from questions.models import Question

def pick_random_question():
    return random.choice(Question.objects.all())

def calculate_score(answers):
    return sum(1 for a in answers if a['correct']) + 10