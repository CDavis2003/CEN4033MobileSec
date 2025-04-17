import random
from questions.models import Question

def pick_random_questio():
    return random.choice(Question.objects.all())