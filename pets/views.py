from django.shortcuts import render
from .models import Pet


def get_pets(request):
    queryset = Pet.objects.all()
    return render(request, "pets.html", {"pets": list(queryset)})
