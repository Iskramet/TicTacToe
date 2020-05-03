from django.urls import path

from . import views

urlpatterns = [
    path('', views.HelloPage.as_view()),
    path('questions/', views.QuestionsPage.as_view(), name='questionpage'),
]