from django.shortcuts import render

# Create your views here.

# HTTP REQUEST


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Bruno Mendes',
    })
