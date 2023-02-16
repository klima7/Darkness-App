from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Pair


@login_required
def index(request):
    pairs_raw = Pair.objects.all()
    pairs_tmp = {(pair.first, pair.second): pair for pair in pairs_raw}
    pairs = {first: {second: pairs_tmp[(first, second)] for second in Pair.LETTERS} for first in Pair.LETTERS}
    return render(request, 'board/index.html', context={'pairs': pairs, 'letters': Pair.LETTERS})
