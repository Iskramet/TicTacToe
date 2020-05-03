from django import forms

from .models import Answer, Questions

class MainForm(forms.Form):
    name = forms.CharField()
    answer = forms.CharField()
    answer1 = forms.CharField()
    answer2 = forms.CharField()
    answer3 = forms.CharField()
    answer4 = forms.CharField()