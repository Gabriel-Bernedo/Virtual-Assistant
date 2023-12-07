from django.contrib import admin
from .models.Question import Question
from .models.Section import Section
# Register your models here.
admin.site.register(Question)
admin.site.register(Section)


