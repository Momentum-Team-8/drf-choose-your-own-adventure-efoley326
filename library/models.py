from django.db import models
from django.db.models import constraints, ManyToOneRel
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book(models.Model):

    author = models.CharField(max_length=200)
    title = models.ForeignKey("Library", on_delete=models.CASCADE, related_name="book")
    genre = models.CharField(max_length=250)
    featured = models.BooleanField(default=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='no_repeats')
        ]

    def __str__(self):
        return {self.title}
class Library(models.Model):
    book_profile = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="bookinfo")

    def __init__(self, author, title, genre, featured):
        self.author = author
        self.title = title
        self.genre = genre
        self.featured = featured
            
    def __str__(self):
        return {self.book_profile}