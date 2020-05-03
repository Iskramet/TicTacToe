from django.db import models

class Questions(models.Model):
    questions_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer_name = models.CharField(max_length=100)
    answer_corectly = models.TextField()
    answer_corectly1 = models.TextField()
    answer_corectly2 = models.TextField()
    answer_corectly3 = models.TextField()
    answer_corectly4 = models.TextField()