
# Register your models here.
from django.contrib import admin

# to link models to admin.py
from .models import Question
from .models import Choice
# link Question Choice model to admin
# admin.site.register(Question)
admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
# Django was able to construct a default form representation. to edit, replace admin.site.register(Question) to below:
class QuestionAdmin(admin.ModelAdmin):
    # list page
    list_display = ('question_text','pub_date','was_published_recently')
    # edit page
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ]
    inlines =[ChoiceInline]

admin.site.register(Question, QuestionAdmin)
