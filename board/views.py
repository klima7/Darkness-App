from django.shortcuts import render
from core.models import Pair


def index(request):
    pairs_raw = Pair.objects.all()
    pairs_tmp = {(pair.first.char, pair.second.char): pair for pair in pairs_raw}
    pairs = {first: {second: pairs_tmp[(first, second)] for second in Pair.LETTERS} for first in Pair.LETTERS}
    return render(request, 'board/index.html', context={'pairs': pairs, 'letters': Pair.LETTERS})
