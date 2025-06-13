import random

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Pair

from .serializers import PairSerializer

class RandomPairView(APIView):
    def get(self, request):
        # Get all pairs that have a best word
        pairs = Pair.objects.filter(best__isnull=False)
        
        if not pairs.exists():
            return Response(
                {'error': 'No pairs with best words found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
            
        # Get a random pair
        random_pair = random.choice(list(pairs))
        serializer = PairSerializer(random_pair)
        return Response(serializer.data)
