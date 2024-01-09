# bookapp/models.py

from django.db import models

class Book(models.Model):
    name= models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.title}"

