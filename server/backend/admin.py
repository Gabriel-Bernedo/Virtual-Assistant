from django.contrib import admin
from django import forms
from .models.Subject import Subject
from .models.Information import Information
from .models.Question import Question
from .models.Answer import Answer
from django.forms import inlineformset_factory
from django.forms import BaseModelFormSet

AnswerFormSet = inlineformset_factory(Question, Answer, fields=["answer_text"])

class MyAdminFormSet(BaseModelFormSet):
    pass



class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = []

class SubjectAdmin(admin.ModelAdmin):
    #def get_changelist_formset(self, request, **kwargs):
    #    kwargs["formset"] = AnswerFormSet
    #    return super().get_changelist_formset(request, **kwargs)

    list_display = ["subject_parent", "subject_name"]
    fields = [("subject_name","subject_nickname"),"subject_parent"]
    #form = SubjectForm
    
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Information)
admin.site.register(Question)
admin.site.register(Answer)

# Register your models here.
