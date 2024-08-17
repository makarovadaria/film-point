import random

from events.api import get_film_list_by_filter, get_film_list_mock
from .models import Movie
from django.shortcuts import render

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
    region = request.GET.get('region')
    filter["region"] = region

    # if len(filter) < 4 :
    #     return render(request, 'events/index.html')
    #
    # years_str = filter.get("years", "")
    # if '-' in years_str:
    #     start_year, end_year = map(str, years_str.split('-'))
    #     filter["release_date_gte"] = start_year + "-01-01"
    #     filter["release_date_lte"] = end_year + "-12-31"
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
