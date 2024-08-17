from django.db import models

class UserAnswer(models.Model):
    user_id = models.CharField(max_length=100)  # Replace with appropriate user identification
    question_type = models.CharField(max_length=50)
    answer = models.CharField(max_length=255)
    # timestamp = models.DateTimeField(auto_now_add=True)

class MoviePreference(models.Model):
    user_id = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    year_range = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

class Amenities(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    year = models.TextField()
    image = models.CharField(max_length=500)
    rating = models.IntegerField(default=0)
    genre = models.CharField(max_length=250)
    amenities = models.ManyToManyField(Amenities)

    def __str__(self):
        return self.movie_name


class User(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    birthday = models.DateField()

    def __str__(self):
        return self.user_name



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.comment


class Question(models.Model):
    question = models.CharField(max_length=128)
    score = models.IntegerField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=128)

    def __str__(self):
        return self.answer
