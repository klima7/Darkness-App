from rest_framework import serializers
from .models import Pair, Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'description']

class PairSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)
    best_word = WordSerializer(source='best', read_only=True)
    
    class Meta:
        model = Pair
        fields = ['first', 'second', 'words', 'best_word'] 