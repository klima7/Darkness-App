import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Pair


@login_required
def index(request):
    from_letter = request.GET.get('from', 'a')
    to_letter = request.GET.get('to', 'z')

    matching_pairs = list(Pair.objects.filter(first__gte=from_letter, first__lte=to_letter).exclude(best__isnull=True).all())

    count = min(36, len(matching_pairs))
    random_pairs = random.sample(matching_pairs, k=count)
    random.shuffle(random_pairs)
    return render(request, 'random_cards/index.html', {'pairs': random_pairs, 'letters': Pair.LETTERS.upper()})
