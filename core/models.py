from django.db import models


class Pair(models.Model):
    first = models.CharField(max_length=1)
    second = models.CharField(max_length=1)

    @property
    def both(self):
        return f'{self.first}{self.second}'

    def __str__(self):
        return self.both


class Word(models.Model):
    pair = models.ForeignKey(Pair, related_name='words', on_delete=models.CASCADE, null=False)
    word = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=50, null=True, blank=True)
    best = models.BooleanField()

    def __str__(self):
        return self.word
