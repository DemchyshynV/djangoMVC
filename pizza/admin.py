from django.contrib import admin

from .models import PizzaShopModel, PizzaModel, OrderModel

# Register your models here.
admin.site.register(PizzaShopModel)
admin.site.register(PizzaModel)


# admin.site.register(OrderModel)
@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pizza', 'name', 'phone']
