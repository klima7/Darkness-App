from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Letter, Face, Pair
from .serializers import PairSerializer


def index(request, character=None):
    if character is None:
        return redirect('faces:index_with_character', character='a')
    
    letters = Letter.objects.values_list('char', flat=True)
    
    pairs = Pair.objects.filter(
        first__char__iexact=character
    ).select_related(
        'first__face',
        'first__face__color',
        'second__face',
        'second__face__color',
        'best'
    )
    
    # Split pairs into two lists based on second letter's face position
    ufd_pairs = []  # Up, Front, Down
    lrb_pairs = []  # Left, Right, Back
    
    for pair in pairs:
        position = pair.second.face.position
        if position in ['U', 'F', 'D']:
            ufd_pairs.append(pair)
        elif position in ['L', 'R', 'B']:
            lrb_pairs.append(pair)
    
    context = {
        'ufd_pairs': ufd_pairs,
        'lrb_pairs': lrb_pairs,
        'letters': letters,
        'current_letter': character,
    }
        
    return render(request, 'faces/index.html', context=context)
