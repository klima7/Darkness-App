from rest_framework import serializers
from core.models import Pair, Word, Letter

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ['char']

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'description']
        

class PairSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)
    best_word = WordSerializer(source='best', read_only=True)
    first = LetterSerializer(read_only=True)
    second = LetterSerializer(read_only=True)
    
    class Meta:
        model = Pair
        fields = ['id', 'first', 'second', 'words', 'best_word', 'difficult'] 