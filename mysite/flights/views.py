from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport


# Create your views here.
def index(request):
    return HttpResponse('Наша первая страница')


def airports(request):
    a = Airport.objects.all()
    context = {
        "airports": a
    }
    return render(request, 'airports.html', context)
