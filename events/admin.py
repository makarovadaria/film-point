from django.contrib import admin
from .models import SurveyQuestion


class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('stage', 'question', 'filter')


admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
