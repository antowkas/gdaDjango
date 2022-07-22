from django.test import TestCase, Client
from .models import Airport, Flight


# Create your tests here.
class FlightTestCase(TestCase):
    def setUp(self):
        a = Airport.objects.create(name="AAA", city="A")
        b = Airport.objects.create(name="BBB", city="B")
        Flight.objects.create(origin=a, destination=b, duration=2)

    def test_valid_flight(self):
        a = Airport.objects.create(name="AAA", city="A")
        b = Airport.objects.create(name="BBB", city="B")
        f = Flight.objects.create(origin=a, destination=b, duration=3)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight(self):
        a = Airport.objects.create(name="AAA", city="A")
        b = Airport.objects.create(name="BBB", city="A")
        f = Flight.objects.create(origin=a, destination=a, duration=3)
        self.assertFalse(f.is_valid_flight())

    def test_airports_view(self):
        c = Client()
        response = c.get("/flights/airports/")
        self.assertEqual(response.status_code, 200)
