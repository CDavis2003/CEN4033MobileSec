from django.shortcuts import render, redirect
from .forms import QuestionForm


def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions:success')  # Or wherever you want to go after
    else:
        form = QuestionForm()

    return render(request, 'add_question.html', {'form': form})

def success(request):
    return render(request, 'success.html')