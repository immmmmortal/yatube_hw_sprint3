from django.contrib.auth.models import User
from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=48)
    description = models.TextField()
    group_image = models.ImageField()

    def __str__(self):
        return self.title


class Author(User):
    pass

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=48)
    post_image = models.ImageField(upload_to='images/')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='author')
    added_date = models.DateTimeField(auto_created=True, blank=True, null=True)
    edited_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
