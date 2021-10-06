from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.TextField()
    director = models.TextField()
    is_favorite = models.BooleanField()


def create_movie(title, genre, director, is_favorite):
    movie = Movie(title=title, genre=genre, director=director, is_favorite=is_favorite)
    movie.save()
    return "{{title}} has been added to your list!"

def all_movies():
    return Movie.objects.all()

def filter_by_genre(genre):
    return Movie.objects.filter(genre=genre)

def filter_by_director(director):
    return Movie.objects.filter(director=director)

def filter_favorites():
    return Movie.objects.filter(is_favorite=True)

def search_by_title(title):
    return Movie.objects.get(title=title)

def update_movie(title, genre, director, is_favorite):
    movie = search_by_title(title)
    movie.genre = genre
    movie.director = director
    movie.is_favorite = is_favorite
    movie.save()
    return "{{title}} has been updated!"

def delete_movie(title):
    movie = search_by_title(title)
    movie.delete()
    return "{{title}} has been deleted!"