from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField()
