from django.shortcuts import render, redirect
from random import uniform

from .models import Questions, Answer
from .forms import MainForm

def ran(request):
    count = Questions.objects.count()
    count_finish = int(uniform(1, count))
    return redirect('main', count_finish)


def main(request, count):
    if request.method == "POST":
        form = MainForm(request.POST)
        if form.is_valid():
            answer_user = form.cleaned_data.get('name')
            answer = form.cleaned_data.get('answer')
            quest = Questions.objects.get(questions_id = count)
            b = Answer(answer_name = answer_user, answer_question = quest, answer_corectly = answer)
            b.save()
            return render(request, 'templates/thanks.html')
    else:
        answer = Questions.objects.get(questions_id = count)
        form = MainForm()
    data = {
        "answer": answer,
        "form": form,
    }
    return render(request, 'templates/main.html', data)