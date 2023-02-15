from rest_framework import serializers
from core.models import Pair, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        exclude = ['pair']


class PairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'

    words = WordSerializer(many=True)
