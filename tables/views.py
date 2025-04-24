from django.shortcuts import render
from core.models import Face


def index(request):
    faces = Face.objects.all().prefetch_related('letters', 'letters__pairs_first')

    for face in faces:
        pairs = [list(letter.pairs_first.all()) for letter in face.letters.all()]
        face.zipped = list(zip(*pairs))

    return render(request, 'tables/index.html', context={'faces': faces})
