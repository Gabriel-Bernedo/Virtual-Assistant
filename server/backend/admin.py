from django.contrib import admin
from .models.Subject import Subject
from .models.Information import Information
from .models.Question import Question


admin.site.register(Subject)
admin.site.register(Information)
admin.site.register(Question)

# Register your models here.
