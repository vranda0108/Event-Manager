from rest_framework import viewsets
from .models import Venue, Event, Ticket, EventReview
from .serializers import VenueSerializer, EventSerializer, TicketSerializer, EventReviewSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class EventReviewViewSet(viewsets.ModelViewSet):
    queryset = EventReview.objects.all()
    serializer_class = EventReviewSerializer
