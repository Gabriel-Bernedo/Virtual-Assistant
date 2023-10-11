from rest_framework import serializers
from models.Action import Action
class ActionSerializers(serializers.Serializer):
    class Meta:
        model = Action
        fields = "__all__"