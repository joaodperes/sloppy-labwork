from django.shortcuts import render


def index(request):
    return render(request, 'register/page-home.html', {})
