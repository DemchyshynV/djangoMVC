from django.shortcuts import render

from .models import PizzaShopModel


# Create your views here.

# def index(request):
#     users = [
#         {'name': 'Max', 'age': 15},
#         {'name': 'Kira', 'age': 20},
#         {'name': 'Karina', 'age': 20},
#     ]
#     return render(request, 'index.html', {'users': users})

def pizza_shop(request):
    qs = PizzaShopModel.objects.all()
    # qs = qs.filter(rating__lt=100).order_by('-name')
    # pizza = PizzaShopModel.objects.get(id=1)
    qs = qs[2:3]
    return render(request, 'pizza_phop.html', {'pizza_shops': qs})
