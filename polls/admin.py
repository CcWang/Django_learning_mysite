
# Register your models here.
from django.contrib import admin

# to link models to admin.py
from .models import Question
from .models import Choice
# link Question model to admin
admin.site.register(Question)
admin.site.register(Choice)