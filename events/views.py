from events.api import get_film_list_by_filter
from .models import Movie, SurveyQuestion, SurveyAnswer
from django.shortcuts import render, redirect


def retake_survey(request):
    current_user = request.user
    stage_check = 1
    if request.method == 'POST':
        stage_reset = request.POST.get('reset') == "reset"
        if stage_reset:
            current_user.current_stage = 1
            current_user.save()
            if stage_check == current_user.current_stage:
                return redirect('retake_survey')


def intro_survey(request):
    current_user = request.user
    user_survey_stage = current_user.current_stage
    # This line of code does this and this
    questions = SurveyQuestion.objects.filter(stage=user_survey_stage)
    stage_limit = 4
    if request.method == 'POST' and user_survey_stage < stage_limit:
        submitted_answer = request.POST.get('answer')
        question_id = request.POST.get('question')
        question = questions.get(id=int(question_id))
        SurveyAnswer.objects.create(
            user=current_user,
            question=question,
            answer=submitted_answer
        )
        current_user.current_stage += 1
        current_user.save()
        return redirect('intro_survey')
    elif user_survey_stage == stage_limit:
        return redirect('get_recommendations')
    return render(request, 'events/movie_survey.html', {'questions': questions})


def index(request):
    return render(request, 'events/index.html')


def get_recommendations(request):
    current_user = request.user
    answers = SurveyAnswer.objects.filter(user=current_user)
    answers_list = []
    for answer in answers:
        answers_list.append(answer.answer)
    recommended_movies = get_film_list_by_filter(answers_list)
    return render(
        request,
        'events/recommendation.html',
        {'movie': 'movie', 'recommended_movies': recommended_movies}
    )


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, '', {'movies': movies})


def movie_detail(request, movie_name):
    movie = Movie.objects.get(name=movie_name)
    return render(request, '', {'movie': movie})
