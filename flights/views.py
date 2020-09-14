from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer
from rest_framework.generics import ListAPIView
from datetime import datetime

class FlightList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BookingList(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today().strftime('%Y-%m-%d'))
    serializer_class = BookingSerializer
