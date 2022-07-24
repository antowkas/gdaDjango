from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AirportView, AirportViewset, FlightViewset

urlpatterns = [
    path('airports/', AirportView.as_view())
]

router = DefaultRouter()

router.register('airports2', AirportViewset)
router.register('flights', FlightViewset)

urlpatterns += router.urls
