import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Pair


@login_required
def index(request):
    from_letter = request.GET.get('from', 'a')
    to_letter = request.GET.get('to', 'z')
    print(from_letter, to_letter)
    pks = Pair.objects.values_list('id', flat=True)
    pks = random.sample(list(pks), k=36)
    pairs = list(Pair.objects.filter(id__in=pks).all())
    random.shuffle(pairs)
    return render(request, 'random_cards/index.html', {'pairs': pairs, 'letters': Pair.LETTERS.upper()})
