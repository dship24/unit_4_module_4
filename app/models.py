from django.db import models

class Project(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    num_pages = models.PositiveIntegerField()
    published_date = models.DateField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"