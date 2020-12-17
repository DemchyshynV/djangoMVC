from django.contrib import admin

from .models import PizzaShopModel, PizzaModel

# Register your models here.
admin.site.register(PizzaShopModel)
admin.site.register(PizzaModel)
