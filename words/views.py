import random

from django.shortcuts import render
from core.models import Pair, Letter


def index(request):
    from_char = request.GET.get('from', 'a')
    to_char = request.GET.get('to', 'z')
    count = int(request.GET.get('count', '36'))
    difficulty = request.GET.get('difficulty', 'all')

    from_letter = Letter.objects.filter(char=from_char).get()
    to_letter = Letter.objects.filter(char=to_char).get()

    letters = list(Letter.objects.filter(order__gte=from_letter.order, order__lte=to_letter.order).all())
    matching_pairs = list(Pair.objects.filter(first__in=letters).exclude(best__isnull=True).all())
    
    if difficulty == 'difficult':
        matching_pairs = [pair for pair in matching_pairs if pair.difficult]

    count = min(count, len(matching_pairs))
    random_pairs = random.sample(matching_pairs, k=count)
    random.shuffle(random_pairs)
    context = {
        'pairs': random_pairs,
        'letters': Letter.objects.all(),
        'counts': [36, 72, 108, 144, 1000],
        'difficulty': difficulty
    }
    return render(request, 'words/index.html', context)
