from django.db import models
from authentication.models import Account
from django.urls import reverse
# from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    # can do default=timezone.now argument to allow for changeable date_posted
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Return to post-detail page upon successful post creation
        # return reverse("post-detail", kwargs={"pk": self.pk})
        return reverse('blog-home')
