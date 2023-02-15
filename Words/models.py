from django.db import models


class Pair(models.Model):
    first = models.CharField(max_length=1)
    second = models.CharField(max_length=1)
    best = models.ForeignKey('Word', related_name='+', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.first}{self.second}'


class Word(models.Model):
    pair = models.ForeignKey(Pair, related_name='words', on_delete=models.CASCADE, null=False)
    word = models.CharField(max_length=20, blank=False)
    description = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.word
