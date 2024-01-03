from django.shortcuts import get_object_or_404


from ..models.Subject import Subject
from ..models.Information import Information
from ..models.Question import Question

from ..serializers.Information import InfoSerializer

from rest_framework import viewsets
from rest_framework.response import Response

class InfoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
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