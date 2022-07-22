from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport, Flight, Passanger
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return HttpResponse('Наша первая страница')


# @permission_required("flights.view_aiport", raise_exception=True)
def airports(request):
    a = Airport.objects.all()
    context = {
        "airports": a
    }
    return render(request, 'airports.html', context=context)


@login_required
def date_time_filter(request):
    if request.method == "GET":
        start_date = request.GET.get("start")
        f = None
        if start_date:
            f = Flight.objects.filter(created_at__gte=start_date)
        context = {
            "flights": f,
            "date": start_date
        }
    return render(request, "date_filter.html", context=context)


def passanger(request, slug):
    p = get_object_or_404(Passanger, slug=slug)
    return HttpResponse(p.first_name)
