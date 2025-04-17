from django.shortcuts import render, redirect
from .models import Game
from questions.models import Question
import random


def play_game(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        user_answer = request.POST.get('answer') == 'True'
        question = Question.objects.get(id=question_id)
        is_correct = (user_answer == question.correct_answer)

        game = Game.objects.create(
            user=request.user,
            question=question,
            is_correct=is_correct,
            score=10 if is_correct else 0
        )
        return redirect('game-result', game_id=game.id)

    # GET - serve a random question
    question = random.choice(Question.objects.all())
    return render(request, 'game/play.html', {'question': question})


def game_result(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'game/result.html', {'game': game})
