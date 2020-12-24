from django.shortcuts import render

from .models import PizzaShopModel
from .forms import OrderForm


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
    # qs = qs[2:3]
    form = OrderForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'pizza/pizza_phop.html', {'pizza_shops': qs, 'form': form})


# def pizza(request, string, id):
#     print(id)
#     print(string)
#     return render(request, 'pizza.html', {})

def pizza(request, id):
    try:
        qs = PizzaShopModel.objects.get(pk=id).pizzas.all()
        # qs = qs.pizzas.all()
    except Exception:
        qs = None
    print(qs)
    return render(request, 'pizza/pizza.html', {'pizzas': qs})
