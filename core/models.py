from django.db import models
from rest_framework.exceptions import ValidationError


class Word(models.Model):
    pair = models.ForeignKey('Pair', related_name='words', on_delete=models.CASCADE, null=False)
    word = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.word


class Pair(models.Model):

    LETTERS = 'abcdefghijklłmnoprstuwz'
    FIRST_CHOICES = ((char, char) for char in LETTERS)
    SECOND_CHOICES = ((char, char) for char in LETTERS)

    first = models.CharField(max_length=1, choices=FIRST_CHOICES, null=False, blank=False)
    second = models.CharField(max_length=1, choices=SECOND_CHOICES, null=False, blank=False)
    best = models.ForeignKey(Word, related_name='abc', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def both(self):
        return f'{self.first}{self.second}'

    def __str__(self):
        return self.both

    def clean(self):
        if self.best is not None and self.best not in self.words.all():
            raise ValidationError('Best word must be a standard word for given pair')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
