from django.shortcuts import render, redirect
from random import uniform
from django.views.generic import View, TemplateView

from .models import Questions, Answer
from .forms import MainForm

class HelloPage(TemplateView):

    template_name = "hello.html"

    def ran(request):
        count = Questions.objects.count()
        count_finish = int(uniform(1, count))
        return redirect('main', count_finish)



class QuestionsPage(View):

    def get(self, request):
        a = 0
        answerbd = Questions.objects.all()[:5]
        for answer in answerbd:
            if a == 0:
                answer0 = answer
            elif a == 1:
                answer1 = answer
            elif a == 2:
                answer2 = answer
            elif a == 3:
                answer3 = answer
            elif a == 4:
                answer4 = answer
            a += 1
        form = MainForm()
        data = {
            "answer0": answer0,
            "answer1": answer1,
            "answer2": answer2,
            "answer3": answer3,
            "answer4": answer4,
            "form": form,
        }
        return render(request, 'questions_page.html', data)

    def post(self, request):
        form = MainForm(request.POST)
        if form.is_valid():
            answer_user = form.cleaned_data.get('name')
            answer = form.cleaned_data.get('answer')
            answer1 = form.cleaned_data.get('answer1')
            answer2 = form.cleaned_data.get('answer2')
            answer3 = form.cleaned_data.get('answer3')
            answer4 = form.cleaned_data.get('answer4')
            b = Answer(answer_name = answer_user, answer_corectly = answer, answer_corectly1 = answer1, answer_corectly2 = answer2, answer_corectly3 = answer3, answer_corectly4 = answer4)
            b.save()
            return render(request, 'thanks.html')

        data = {
            "answer": answer,
            "form": form,
        }
        return render(request, 'questions_page.html', data)