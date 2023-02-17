import random

from django.shortcuts import render
from core.models import Pair, Letter


def index(request):
    from_char = request.GET.get('from', 'a')
    to_char = request.GET.get('to', 'z')

    from_letter = Letter.objects.filter(char=from_char).get()
    to_letter = Letter.objects.filter(char=to_char).get()

    letters = list(Letter.objects.filter(order__gte=from_letter.order, order__lte=to_letter.order).all())
    matching_pairs = list(Pair.objects.filter(first__in=letters).exclude(best__isnull=True).all())

    count = min(36, len(matching_pairs))
    random_pairs = random.sample(matching_pairs, k=count)
    random.shuffle(random_pairs)
    return render(request, 'random_cards/index.html', {'pairs': random_pairs, 'letters': Letter.objects.all()})
