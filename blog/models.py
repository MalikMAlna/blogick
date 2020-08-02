from django.contrib.auth.models import User
from django.db import models
# from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    # can do default=timezone.now argument to allow for changeable date_posted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_last_modifed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
