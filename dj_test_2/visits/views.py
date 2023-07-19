from django.shortcuts import render
from .models import Visit


def index(request, page="index"):
    v = Visit(page=page)
    if request.user.is_authenticated:
        v.username = request.user.username
    v.save()

    visitors = Visit.objects.filter(page=page)

    context = {
        "page": page,
        "visitors": visitors,
        "num_visits": visitors.count(),
    }
    return render(request, "index.html", context)