from django.shortcuts import render
from core.models import Pair, Letter


def index(request):
    letters = list(Letter.objects.all())
    pairs_raw = Pair.objects.all()
    pairs_tmp = {(pair.first, pair.second): pair for pair in pairs_raw}
    pairs = {first: {second: pairs_tmp[(first, second)] for second in letters} for first in letters}
    return render(request, 'board/index.html', context={'pairs': pairs, 'letters': letters})
