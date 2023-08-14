from rest_framework import serializers
from restaurant.models import Menu, Booking 

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']