from django import forms


class GenreForm(forms.Form):
    genre = forms.ChoiceField(choices=[
        ('action', 'Action - Spicy and thrilling!'),
        ('comedy', 'Comedy - Sweet and delightful!'),
        ('drama', 'Drama - Rich and full-bodied!'),
        ('horror', 'Horror - Bitter and bone-chilling!'),
        ('romance', 'Romance - Sweet with a hint of spice!'),
        ('scifi', 'Sci-Fi - Zesty and out-of-this-world!'),
    ])


class ReleaseDate(forms.Form):
    release_date = forms.ChoiceField(choices=[
        ('1920-1950', '1920s - silent spice'),
        ('1950-1979', '1950-1979 - golden oldies'),
        ('1980-1989', '1980-1989 - cult classics'),
        ('1990-1999', '1990-1999 - nostalgic hits'),
        ('2000-2019', '2000-2019 - millennial magic'),
        ('2020-2024', '2020+ - modern marvels'),
    ])


class MovieRegion(forms.Form):
    movie_region = forms.ChoiceField(choices=[
        ('us', 'Hollywood and its many USA buddies'),
        ('india', 'Bollywood (India)'),
        ('europe', 'European Studios'),
        ('asia', 'Asian Studios (excluding Bollywood)'),
        ('latam', 'Latin American Studios'),
        ('none', 'I don’t care, as long as it’s good!'),
    ])
