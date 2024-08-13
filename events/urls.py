from django.urls import path
from events import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey/', views.survey, name='survey'),
    path('get_result/', views.get_result, name='get_result'),
    path('get_recommendations/', views.get_recommendations, name='get_recommendations'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]
