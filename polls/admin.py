from django.contrib import admin
from . import models

class ChoiceInline(admin.TabularInline):
    model=models.Choice
    extra= 1

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    # model = models.Question
    list_display=('id','question_text','pub_date')
    list_filter= ('pub_date','question_text')
    inlines = [ChoiceInline]
@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    model=models.Choice
    list_display=('question_id', 'choice_text','vote')
    list_filter = ('choice_text','vote')
