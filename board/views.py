from django.shortcuts import render
from core.models import Pair, Letter


def index(request):
    letters = list(Letter.objects.all())
    pairs_raw = Pair.objects.all()
    pairs_tmp = {(pair.first, pair.second): pair for pair in pairs_raw}
    pairs = {row: {column: pairs_tmp[(column, row)] for column in letters} for row in letters}
    return render(request, 'board/index.html', context={'pairs': pairs, 'letters': letters})
