from django.shortcuts import render
from .models import Visits


def index(request):
    v = Visits.objects.first()
    v.count += 1
    v.save()

    context = {
        "num_visits": v.count,
    }
    return render(request, "index.html", context)