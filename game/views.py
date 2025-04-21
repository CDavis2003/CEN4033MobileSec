from django.shortcuts import render, redirect
from .models import Game
from questions.models import Question
from .utils import pick_random_question, calculate_score

def play_game(request):
    user = request.user

    # Initialize session tracking
    if "score" not in request.session:
        request.session["score"] = 0
    if "answered_questions" not in request.session:
        request.session["answered_questions"] = []

    answered_ids = request.session["answered_questions"]
    remaining_questions = Question.objects.exclude(id__in=answered_ids)

    if not remaining_questions.exists():
        final_score = request.session["score"]
        request.session["score"] = 0
        request.session["answered_questions"] = []
        return render(request, "game_over.html", {"final_score": final_score})

    feedback = None
    current_score = request.session["score"]

    if request.method == "POST":
        selected_answer = request.POST.get("selected_answer")
        question_id = request.POST.get("question_id")
        question = Question.objects.get(id=question_id)

        is_correct = str(question.correct_answer).lower() == selected_answer.lower()
        is_correct = str(question.correct_answer).lower() == selected_answer.lower()
        if is_correct:
            request.session["score"] += 10
            feedback = "Correct!"
        else:
            feedback = f"Incorrect. {question.feedback_text}"

        Game.objects.create(user=user, question=question, is_correct=is_correct, score=request.session["score"])
        request.session["answered_questions"].append(question.id)
        request.session.modified = True

        # Fetch next question after answering
        remaining_questions = Question.objects.exclude(id__in=request.session["answered_questions"])
        if not remaining_questions.exists():
            final_score = request.session["score"]
            request.session["score"] = 0
            request.session["answered_questions"] = []
            return render(request, "game_over.html", {"final_score": final_score})
        next_question = remaining_questions.order_by("?").first()

        return render(request, "play.html", {
            "question": next_question,
            "score": request.session["score"],
            "feedback": feedback
        })

    # First time loading
    next_question = remaining_questions.order_by("?").first()
    return render(request, "play.html", {
        "question": next_question,
        "score": current_score,
        "feedback": None
    })
