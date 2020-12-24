from django.shortcuts import render

from .models import PetModel, OwnerModel


# Create your views here.
def home(request):
    return render(request, 'index.html')


def owners(request):
    qs = OwnerModel.objects.all()
    return render(request, 'owners.html', {'owners': qs})


def pets(request):
    qs = PetModel.objects.all()
    return render(request, 'pets.html', {'pets': qs})
