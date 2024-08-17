import random

from events.api import get_film_list_by_filter, get_film_list_mock
from .models import Movie
from django.shortcuts import render

# Marianna: With changes will rather be:
from django.shortcuts import render, redirect
from .forms import GenreForm, ReleaseDate, MovieRegion
from .models import UserAnswer, Movie
import requests

def survey1(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            # Save user answer to database
            user_answer = UserAnswer(
                user_id=request.user.id,  # Replace with user authentication
                question_type='genre',
                answer=form.cleaned_data['genre']
            )
            user_answer.save()
            return redirect('survey2')
    else:
        form = GenreForm()
    return render(request, 'movie_survey1.html', {'form': form})

def survey2(request):
    if request.method == 'POST':
        form = ReleaseDate(request.POST)
        if form.is_valid():
            # Save user answer to database
            user_answer = UserAnswer(
                user_id=request.user.id,  # Replace with user authentication
                question_type='year_range',
                answer=form.cleaned_data['year_range']
            )
            user_answer.save()
            return redirect('survey3')
    else:
        form = ReleaseDate()
    return render(request, 'movie_survey2.html', {'form': form})

def survey3(request):
    if request.method == 'POST':
        form = MovieRegion(request.POST)
        if form.is_valid():
            # Save user answer to database
            user_answer = UserAnswer(
                user_id=request.user.id,  # Replace with user authentication
                question_type='region',
                answer=form.cleaned_data['region']
            )
            user_answer.save()
            return redirect('survey_result')
    else:
        form = MovieRegion()
    return render(request, 'movie_survey3.html', {'form': form})
# Similar views for survey3

filter = {}
def index(request):
    return render(request, 'events/index.html')
def survey(request):

    return render(request, 'events/movie_survey1.html')
def survey_genre(request):
    genre = request.GET.get('genres')
    filter["genre"] = genre

    return render(request, 'events/movie_survey2.html')
def survey_year(request):
    years = request.GET.get('years')
    filter["years"] = years
    return render(request, 'events/movie_survey3.html')
def survey_region(request):
    # region = request.GET.get('region')
    # filter["region"] = region
    #
    # years_str = filter.get("years", "")
    # if '-' in years_str:
    #     start_year, end_year = map(str, years_str.split('-'))
    #     filter["release_date_gte"] = start_year + "-01-01"
    #     filter["release_date_lte"] = end_year + "-12-31"
    #
    # if len(filter) < 4:
    #     return render(request, 'events/index.html')
    #
    # movie_list = get_film_list_by_filter(filter)
    movie_list = get_film_list_mock(filter)
    return render(request, 'events/movie_survey_result.html', {'movie_list': movie_list})

def recommendation(request):
    return render(request, 'events/recommendation.html')


# def survey(request):
#     if request.method == 'POST':
#         form = MovieSurveyForm(request.POST)
#         if form.is_valid():
#             genre = form.cleaned_data['genre']
#             moods = form.cleaned_data['moods']
#             pace = form.cleaned_data['pace']
#             age = form.cleaned_data['age_group']
#
#             recommended_movies = Movie.objects.filter(genre=genre, mood=moods, pace=pace, age_group=age)
#             return render(request, '', )
#
#         else:
#             form = MovieSurveyForm()
#
#         return render(request, '', {'form': form})


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
