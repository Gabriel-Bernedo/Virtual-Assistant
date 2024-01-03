from rest_framework import serializers
from ..models.Information import Information

class InfoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Information
    fields = "__all__"