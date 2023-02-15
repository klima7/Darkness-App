from rest_framework import serializers
from .models import Pair, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'description']


class PairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'

    best = WordSerializer()
    words = WordSerializer(many=True)
