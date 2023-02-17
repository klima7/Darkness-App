from django.shortcuts import render
from core.models import Face


def index(request):
    faces = Face.objects.all()

    for face in faces:
        pairs = [list(letter.pairs_first.all()) for letter in face.letters.all()]
        face.zipped = list(zip(*pairs))
        print(face.zipped)

    return render(request, 'tables/index.html', context={'faces': faces})
