import requests
from events.api import get_film_list_by_filter
from .models import Movie, SurveyQuestion
from .forms import GenreForm, ReleaseDate, MovieRegion
from django.shortcuts import redirect, render


def get_movies(genre, year, region):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key=YOUR_API_KEY&with_genres={genre}&primary_release_date.gte={year}-01-01&primary_release_date.lte={year}-12-31&with_original_language={region}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return []  # Handle error


def intro_survey(request):
    current_user = request.user
    user_survey_stage = current_user
    questions = SurveyQuestion.objects.all()
    if request.method == 'POST':
        answer = request.POST.get('answer')

    return render(request, 'events/movie_survey.html', {'questions': questions})


def index(request):
    return render(request, 'events/index.html')


def recommendation(request):
    return render(request, 'events/recommendation.html')


def get_recommendations(request):
    # movie = get_object_or_404(id=movie_name)
    # recommended_movies = Movie.objects.filter(genre=movie.genre).exclude(id=movie.name)

    recommended_movies = get_film_list_by_filter(filter)
    return render(request, '',
                  {'movie': 'movie', 'recommended_movies': recommended_movies})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, '', {'movies': movies})


def movie_detail(request, movie_name):
    movie = Movie.objects.get(name=movie_name)
    return render(request, '', {'movie': movie})
