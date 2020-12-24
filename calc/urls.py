from django.urls import path

from .views import calc

urlpatterns = [
    path('/<int:first>/<str:option>/<int:second>', calc, name='calc')
]
