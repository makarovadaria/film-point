from django.db import models
from django import forms


class Amenities(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movies(models.Model):
    movie_name = models.CharField(max_length=128)
    movie_description = models.TextField()
    movie_image = models.CharField(max_length=500)
    price = models.IntegerField()
    amenities = models.ManyToManyField(Amenities)

    def __str__(self):
        return self.movie_name


class MovieForm(forms.Form):
    title = forms.CharField(max_length=128)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = forms.DateField()
    description = forms.CharField(widget=forms.Textarea, required=False)


