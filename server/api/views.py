from django.http import JsonResponse
from django.views.generic import View

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers.Question import QuestionSerializer
from .models.Question import Question

import json
# RESTFRAMEWORK ViewSets
class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def list(self,request):
        queryset = Question.objects.all()

        serializer = QuestionSerializer(queryset, many=True)
        return JsonResponse({
            "preguntas": serializer.data
        })
    
    def create(self, request):
        data = json.loads(request.body)
        print(f"Data: {data}")
        question = QuestionSerializer(data=data)
        if(question.is_valid()): 
            question.save()
            return JsonResponse({
                "status": 302
            })
        else:
            return JsonResponse({
                "status": 500,
                "errors": question.errors
            })
        
# REST API VIEWSETS

from .functions.data_tree import getDataTree
class ViewQuestions(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(getDataTree("Data", lambda a : "hoja"))
