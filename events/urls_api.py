# events/urls_api.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import VenueViewSet, EventViewSet, TicketViewSet, EventReviewViewSet

router = DefaultRouter()
router.register(r'venues', VenueViewSet, basename='venue')
router.register(r'events', EventViewSet, basename='event')
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'eventreviews', EventReviewViewSet, basename='eventreview')

urlpatterns = [
    path('', include(router.urls)),
]
