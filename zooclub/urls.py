from django.urls import path

from .views import home, owners, pets
urlpatterns = [
    path('', home),
    path('owners', owners),
    path('pets', pets)
]
