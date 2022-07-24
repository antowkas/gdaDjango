from rest_framework import viewsets

from flights.models import Airport, Flight
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AirportSerializer, FlightSerializer


class AirportView(APIView):
    def get(self, request):
        airports = Airport.objects.all()
        serializer = AirportSerializer(airports, many=True)
        return Response({'airports': serializer.data})

    def post(self, request):
        airport = request.data.get('airport')

        serializer = AirportSerializer(data=airport)
        if serializer.is_valid(raise_exception=True):
            saved_data = serializer.save()
        return Response({"success": f"Airport'{saved_data.name}' create succesfully"}, status=201)


class AirportViewset(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class FlightViewset(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
