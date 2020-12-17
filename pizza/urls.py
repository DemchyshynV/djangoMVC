from django.urls import path

from .views import pizza_shop
urlpatterns = [
    path('', pizza_shop)
]
