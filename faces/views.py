from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Letter, Face, Pair
from .serializers import PairSerializer


def index(request):
    faces = Face.objects.all()
    return render(request, 'search/index.html', context={'faces': faces})

class PairLookupView(APIView):
    def get(self, request):
        letter1 = request.GET.get('letter1')
        letter2 = request.GET.get('letter2')
        
        if not letter1 or not letter2:
            return Response(
                {'error': 'Both letter1 and letter2 parameters are required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            first_letter = Letter.objects.get(char=letter1)
            second_letter = Letter.objects.get(char=letter2)
            pair = Pair.objects.get(first=first_letter, second=second_letter)
            serializer = PairSerializer(pair)
            return Response(serializer.data)
        except Letter.DoesNotExist:
            return Response(
                {'error': 'One or both letters not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Pair.DoesNotExist:
            return Response(
                {'error': 'Pair not found for given letters'}, 
                status=status.HTTP_404_NOT_FOUND
            )
