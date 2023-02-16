import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Pair


@login_required
def index(request):
    pks = Pair.objects.values_list('id', flat=True)
    pks = random.sample(list(pks), k=36)
    pairs = list(Pair.objects.filter(id__in=pks).all())
    random.shuffle(pairs)
    return render(request, 'random_cards/index.html', {'pairs': pairs})
