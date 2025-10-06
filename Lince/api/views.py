from rest_framework import viewsets
from .models import InformeTrimestral, Action
from .serializers import InformeTrimestralSerializer, ActionSerializer
from django.http import JsonResponse

class InformeTrimestralViewSet(viewsets.ModelViewSet):
    queryset = InformeTrimestral.objects.all()
    serializer_class = InformeTrimestralSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer