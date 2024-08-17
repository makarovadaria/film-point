import os
import json
import random

from django.conf import settings
import requests

from events.models import Movie



API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMTYxYzYxMmJjM2UyYjdlMWZiYzgxMjdmYWY0M2I0NiIsIm5iZiI6MTcyMzgwOTgwMC4wNDkxMTksInN1YiI6IjY2YmRkYjAyNTNhNTI1NTY4NmUxNDdiYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c9YAGpSr1isIluCE77kzgro9UvlmIy0e-fRqqoPVkfM'
API_URL = 'https://api.themoviedb.org/3'

regions={}
regions["us"] = "US"
regions["india"] = "IN"
regions["europe"] = "FR"
regions["asia"] = "JP"
regions["latam"] = "BR"

genres={}
genres["action"] = 28
genres["comedy"] = 35
genres["drama"] = 18
genres["horror"] = 27
genres["romance"] = 10749
genres["scifi"] = 878


genres_file_path = os.path.join(settings.BASE_DIR, 'static/film-point/genres.json')
with open(genres_file_path, 'r') as f:
    genres_data = json.load(f)

GENRE_MAP = {genre['id']: genre['name'] for genre in genres_data['genres']}




def get_film_list_mock(filter):
    file_path = os.path.join(settings.BASE_DIR, 'test_response.json')
    with open(file_path, 'r') as file:
        data = json.load(file)
        recommended_movies_json = data.get('results', [])
        objects_array = transform_movie_data(recommended_movies_json)
        return random.sample(objects_array, 10)

def get_film_list_by_filter(filter):

    base_url = f"{API_URL}/discover/movie?release_date.gte={filter['release_date_gte']}&release_date.lte={filter['release_date_lte']}&with_genres={genres[filter['genre']]}"
    if filter["region"] != "none":
        base_url += f"&region={regions[filter['region']]}"

    response = requests.get(base_url, headers={'Authorization': f'Bearer {API_KEY}'})

    if response.status_code == 200:
        recommended_movies_json = response.json().get('results', [])
        objects_array = transform_movie_data(recommended_movies_json)
        recommended_movies = random.sample(objects_array, 10)
    else:
        recommended_movies = []
    return recommended_movies


def transform_movie_data(movie_data):
    movies = []
    for data in movie_data:
        name = data.get("title", "")
        image = data.get("poster_path", "")
        genre_ids = data.get("genre_ids", [])
        genre_names = [GENRE_MAP.get(genre_id, "Unknown") for genre_id in genre_ids]
        genre =  ", ".join(map(str, genre_names))
        year = data.get("release_date", "").split("-")[0]
        description = data.get("overview", "")
        rating = data.get("vote_average", 0.0)

        movie = Movie(name=name, image=image, genre = genre, year=year, description=description, rating=rating)
        movies.append(movie)

    return movies
