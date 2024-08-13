from django.http import HttpResponse
from .models import Movie
from .forms import MovieSurveyForm
from django.shortcuts import render, get_object_or_404


def index(request):
    return HttpResponse("Hello, world. You're at the event index.")


def survey(request):
    if request.method == 'POST':
        form = MovieSurveyForm(request.POST)
        if form.is_valid():
            genre = form.cleaned_data['genre']
            moods = form.cleaned_data['moods']
            pace = form.cleaned_data['pace']
            age = form.cleaned_data['age_group']

            recommended_movies = Movie.objects.filter(genre=genre, mood=moods, pace=pace, age_group=age)
            return render(request, '', )

        else:
            form = MovieSurveyForm()

        return render(request, '', {'form': form})


def get_recommendations(request):
    movie = get_object_or_404(id=movie_name)
    recommended_movies = Movie.objects.filter(genre=movie.genre).exclude(id=movie.name)
    return render(request, '',
                  {'movie': movie, 'recommended_movies': recommended_movies})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, '', {'movies': movies})


def movie_detail(request, movie_name):
    movie = Movie.objects.get(name=movie_name)
    return render(request, '', {'movie': movie})
