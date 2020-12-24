from django.shortcuts import render


# Create your views here.

def calc(request, first, option, second):
    res = ''
    if option == 'add':
        res = f'{first} + {second} = {first + second}'
    elif option == 'sub':
        res = f'{first} - {second} = {first - second}'
    elif option == 'multi':
        res = f'{first} * {second} = {first * second}'
    elif option == 'div':
        try:
            res = f'{first} / {second} = {first / second}'
        except ZeroDivisionError:
            res = None
    return render(request, 'calc/calc.html', {'res': res})
