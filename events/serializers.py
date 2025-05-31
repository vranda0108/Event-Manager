from rest_framework import serializers
from .models import Event, Venue, Ticket, EventReview


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(read_only=True)
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(), source='venue', write_only=True
    )
    remaining_tickets = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

    def get_remaining_tickets(self, obj):
        return obj.get_remaining_tickets()


class TicketSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    event_name = serializers.CharField(source='event.name', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class EventReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.CharField(source='reviewer.username', read_only=True)
    event_name = serializers.CharField(source='event.name', read_only=True)

    class Meta:
        model = EventReview
        fields = '__all__'

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
