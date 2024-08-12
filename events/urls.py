from django.urls import path

from events import views

urlpatterns = [
    path('', views.index, name='index'),
    path('survey/', views.survey, name='survey'),
    path('get_result/', views.get_result, name='get_result'),
]
