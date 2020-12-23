from django.urls import path

from .views import pizza_shop, pizza
# urlpatterns = [
#     path('', pizza_shop),
#     path('/<int:id>/<str:string>', pizza, name='pizza')
# ]
urlpatterns = [
    path('', pizza_shop),
    path('/<int:id>', pizza, name='pizza')
]
