from django.db import models
from django.contrib.auth.models import User
from post.models import Post


# uploading user files to a specific directory
def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=80, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    bio = models.TextField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    saved = models.ManyToManyField(Post)

    def __str__(self):
        return self.first_name
