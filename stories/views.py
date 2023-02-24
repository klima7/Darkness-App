import random

from django.shortcuts import render
from core.models import Letter, Pair


LENGTHS = list(range(4, 21))
STORIES_COUNT = 16


def index(request):
    from_char = request.GET.get('from', 'a')
    to_char = request.GET.get('to', 'z')
    length = int(request.GET.get('length', '8'))
    reveal = bool(int(request.GET.get('reveal', '0')))

    from_letter = Letter.objects.filter(char=from_char).get()
    to_letter = Letter.objects.filter(char=to_char).get()

    letters = list(Letter.objects.filter(order__gte=from_letter.order, order__lte=to_letter.order).all())
    matching_pairs = list(Pair.objects.filter(first__in=letters).exclude(best__isnull=True).all())

    stories = []

    for _ in range(STORIES_COUNT):
        story = random.sample(matching_pairs, k=length)
        random.shuffle(story)
        stories.append(story)

    context = {
        'lengths': LENGTHS,
        'letters': Letter.objects.all(),
        'reveal': reveal,
        'stories': stories
    }
    return render(request, 'stories/index.html', context)
