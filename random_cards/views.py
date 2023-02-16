import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Pair


@login_required
def index(request):
    pks = Pair.objects.values_list('id', flat=True)
    pks = random.choices(pks, k=32)
    pairs = Pair.objects.filter(id__in=pks)
    return render(request, 'random_cards/index.html')
