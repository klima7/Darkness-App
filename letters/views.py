import random

from django.shortcuts import render
from .models import Element, ElementWithFace


def index(request):
    type_ = request.GET.get('type', 'edge')
    count = int(request.GET.get('count', '36'))

    type_ = Element.ElementType.EDGE if type_ == 'edge' else Element.ElementType.CORNER
    elements = list(Element.objects.filter(type=type_).all())
    elements = random.choices(elements, k=count)
    elements_wf = [ElementWithFace(element) for element in elements]

    return render(request, 'letters/index.html', context={'elements':elements_wf})
