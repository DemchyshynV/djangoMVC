from django import forms

from .models import OrderModel


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ('pizza', 'name', 'phone')
