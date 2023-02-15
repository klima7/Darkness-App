from django.db import models


class Pair(models.Model):
    first = models.CharField(max_length=1)
    second = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.first}{self.second}'


class Word(models.Model):
    pair = models.ForeignKey(Pair, related_name='words', on_delete=models.CASCADE, null=False)
    word = models.CharField(max_length=20, blank=False)
    description = models.TextField(null=True, blank=True)
    best = models.BooleanField()

    def __str__(self):
        return self.word
