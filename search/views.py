from django.shortcuts import render

from core.models import Letter, Face


def index(request):
    faces = Face.objects.all()
    return render(request, 'search/index.html', context={'faces': faces})
