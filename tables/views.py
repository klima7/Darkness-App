from django.shortcuts import render
from core.models import Pair


def index(request):
    return render(request, 'tables/index.html')
