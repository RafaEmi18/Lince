from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InformeTrimestralViewSet, ActionViewSet

router = DefaultRouter()
router.register(r'informes', InformeTrimestralViewSet)
router.register(r'actions', ActionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
