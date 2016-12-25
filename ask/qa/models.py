from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    tittle = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, null=False)
    author = models.OneToOneField(User)

class QuestionManager():
    def new():
        return self.order_by('-added_at')

    def popular():
        return self.order_by('-raiting')
