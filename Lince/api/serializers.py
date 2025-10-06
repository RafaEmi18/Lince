from rest_framework import serializers
from .models import InformeTrimestral, Action


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'


class InformeTrimestralSerializer(serializers.ModelSerializer):
    actions = ActionSerializer(many=True, read_only=True)

    class Meta:
        model = InformeTrimestral
        fields = '__all__'
