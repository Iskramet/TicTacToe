from django import forms

from .models import Answer, Questions

class MainForm(forms.Form):
    name = forms.CharField()
    answer = forms.CharField()