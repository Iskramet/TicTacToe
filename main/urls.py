from django.urls import path

from . import views

urlpatterns = [
    path('', views.ran),
    path('<count>', views.main, name='main'),
]