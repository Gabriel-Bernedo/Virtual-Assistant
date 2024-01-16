from django.shortcuts import get_object_or_404

from ..serializers.Information import InfoSerializer, Information
from ..serializers.Question import QuestionSerializer, Question
from ..serializers.Subject import SubjectSerializer, Subject


from rest_framework import viewsets
from rest_framework.response import Response

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InfoSerializer
    """
    A simple ViewSet for listing or retrieving users.
    
    def list(self, request):
        queryset = Information.objects.all()
        serializer = InfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Information.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = InfoSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        data = request.POST
        serializer = InfoSerializer(data=data)
        return Response(serializer.data)
    """

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer