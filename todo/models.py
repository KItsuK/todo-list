from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField('titel', max_length=200)
    memo = models.TextField('memo')
    deadline = models.DateField()

    def __str__(self):
        return self.title
