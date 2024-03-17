from django.db import models
from django.contrib.auth.models import User
from post.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved = models.ManyToManyField(Post)

    # def __str__(self):
    #     return self.user.username
