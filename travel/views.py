from django.shortcuts import render


def home(request):
    name = 'Ivan'
    return render(request, 'home.html', {'name': name })