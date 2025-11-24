from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import InformeTrimestral, Action
from .serializers import InformeTrimestralSerializer, ActionSerializer
from django.http import JsonResponse


class InformeTrimestralViewSet(viewsets.ModelViewSet):
    queryset = InformeTrimestral.objects.all()
    serializer_class = InformeTrimestralSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


@api_view(['GET'])
def api_root(request):
    """
    Punto de entrada de la API. Muestra los endpoints disponibles.
    """
    return Response({
        'message': 'Bienvenido a la API de Lince',
        'version': '1.0',
        'endpoints': {
            'informes': {
                'url': '/api/informes/',
                'description': 'Gestión de informes trimestrales',
                'methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
            },
            'actions': {
                'url': '/api/actions/',
                'description': 'Gestión de acciones',
                'methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
            },
            'admin': {
                'url': '/admin/',
                'description': 'Panel de administración de Django'
            }
        },
        'documentation': 'Accede a cualquier endpoint para ver la interfaz navegable de la API'
    })