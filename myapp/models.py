from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField()


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    name = None
    home_group = models.CharField(max_length=5)
