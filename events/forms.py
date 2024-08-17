from django import forms


class MovieSurveyForm(forms.Form):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
    ]

    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('excited', 'Excited'),
        ('relaxed', 'Relaxed'),
    ]

    PACE_CHOICES = [
        ('slow', 'Slow'),
        ('medium', 'Medium'),
        ('fast', 'Fast'),
    ]

    AGE_GROUP_CHOICES = [
        ('child', 'Child'),
        ('teen', 'Teen'),
        ('adult', 'Adult'),
        ('senior', 'Senior'),
    ]

    genre = forms.ChoiceField(choices=GENRE_CHOICES, label="What genre do you prefer?")
    mood = forms.ChoiceField(choices=MOOD_CHOICES, label="What is your current mood?")
    pace = forms.ChoiceField(choices=PACE_CHOICES, label="What pace do you prefer?")
    age_group = forms.ChoiceField(choices=AGE_GROUP_CHOICES, label="What is your age group?")
