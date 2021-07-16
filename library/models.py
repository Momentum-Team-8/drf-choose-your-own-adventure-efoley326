from django.db import models
from django.db.models import constraints
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=250)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='no_repeats')
        ]

    def __str__(self):
        return {self.title}

class Library(models.Model):
    book_profile = models.CharField(max_length=250)

    def __str__(self):
        return self.book_profile