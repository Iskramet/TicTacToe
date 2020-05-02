from django.db import models

class Questions(models.Model):
    questions_id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer_name = models.CharField(max_length=100)
    answer_question = models.ForeignKey(Questions, on_delete = models.CASCADE, related_name='+')
    answer_corectly = models.TextField()
