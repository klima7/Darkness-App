from rest_framework import serializers
from .models import Pair, Word


class PairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'
