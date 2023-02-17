import random

from django.shortcuts import render
from core.models import Pair


def index(request):
    from_letter = request.GET.get('from', 'a')
    to_letter = request.GET.get('to', 'z')

    from_index = Pair.LETTERS.index(from_letter)
    to_index = Pair.LETTERS.index(to_letter)
    letters = list(Pair.LETTERS[from_index:to_index+1])

    matching_pairs = list(Pair.objects.filter(first__char__in=letters).exclude(best__isnull=True).all())

    count = min(36, len(matching_pairs))
    random_pairs = random.sample(matching_pairs, k=count)
    random.shuffle(random_pairs)
    return render(request, 'random_cards/index.html', {'pairs': random_pairs, 'letters': Pair.LETTERS.upper()})
