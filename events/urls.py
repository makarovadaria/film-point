"""
URL configuration for film_point project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/survey1/', views.survey1, name='survey1'),
    path('test/survey2/', views.survey2, name='survey2'),
    path('test/survey3/', views.survey3, name='survey3'),
    path('test/result/', views.get_movies, name='get_movies'),
    # path('survey/', views.survey, name='survey'),
    # path('get_result/', views.get_result, name='get_result'),
    path('get_recommendations/', views.get_recommendations, name='get_recommendations'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]