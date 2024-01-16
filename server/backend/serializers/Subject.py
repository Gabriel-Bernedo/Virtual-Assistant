from rest_framework import serializers
from ..models.Subject import Subject

class SubjectSerializer(serializers.ModelSerializer):

  class Meta:
    model = Subject
    fields = "__all__"