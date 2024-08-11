from django.db import models


class Amenities(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_name = models.CharField(max_length=128)
    movie_description = models.TextField()
    movie_image = models.CharField(max_length=500)
    movie_rating = models.IntegerField(default=0)
    price = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)

    def __str__(self):
        return self.movie_name


class User(models.Model):
    user_name = models.CharField(max_length=128)
    user_password = models.CharField(max_length=128)
    user_email = models.CharField(max_length=128)
    user_birthday = models.DateField()

    def __str__(self):
        return self.user_name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.movie_name = None

    def __str__(self):
        return self.movie_name


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
