from django.shortcuts import render, redirect
from .models import Game
from questions.models import Question
from .utils import pick_random_question, calculate_score
from random import choice
# from guest_user.decorators import allow_guest_user

# @allow_guest_user
def play_game(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_answer = request.POST.get('answer') == 'True'
        question = Question.objects.get(id=question_id)

        is_correct = question.correct_answer == selected_answer
        score = calculate_score([{'correct': is_correct}])

        Game.objects.create(
            user=request.user,
            question=question,
            is_correct=is_correct,
            score=score
        )
        next_question = pick_random_question()
        return render(request, 'play.html', {
            'question': next_question,
            'last_result': is_correct
        })
    else:
    # GET request: show a random question
        question = pick_random_question()
        return render(request, 'play.html', {
            'question': question,
            'last_result': None  # no result on first GET
        })

# def game_result(request, game_id):
#     game = Game.objects.get(id=game_id)
#     return render(request, 'result.html', {'game': game})
