from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError


class Color(models.Model):
    name = models.CharField(max_length=10, null=False, blank=False)
    red = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)], null=False, blank=False)
    green = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)], null=False, blank=False)
    blue = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)], null=False, blank=False)

    @property
    def rgb(self):
        return f'rgb({self.red}, {self.green}, {self.blue})'

    def __str__(self):
        return self.name


class Face(models.Model):

    class Position(models.TextChoices):
        F = 'F', 'Front'
        B = 'B', 'Back'
        L = 'L', 'Left'
        R = 'R', 'Right'
        U = 'U', 'Up'
        D = 'D', 'Down'

    position = models.CharField(max_length=1, choices=Position.choices, null=False, blank=False)
    color = models.ForeignKey(Color, related_name='faces', on_delete=models.CASCADE, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.get_position_display()


class Letter(models.Model):
    char = models.CharField(max_length=1, null=False, blank=False)
    face = models.ForeignKey(Face, related_name='letters', on_delete=models.CASCADE, null=False, blank=False)
    order = models.IntegerField(null=False, blank=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.char


class Word(models.Model):
    pair = models.ForeignKey('Pair', related_name='words', on_delete=models.CASCADE, null=False)
    word = models.CharField(max_length=20, blank=False, unique=True)
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.word


class Pair(models.Model):
    first = models.ForeignKey(Letter, related_name='pairs_first', on_delete=models.CASCADE, null=False, blank=False)
    second = models.ForeignKey(Letter, related_name='pairs_second', on_delete=models.CASCADE, null=False, blank=False)
    best = models.ForeignKey(Word, related_name='abc', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def both(self):
        return f'{self.first}{self.second}'

    @property
    def tables_tooltip(self):
        result = ''
        if self.best and self.best.description:
            result += self.best.description
        other_words = [word.word for word in self.words.all() if word != self.best]
        if other_words:
            joined_words = ', '.join(other_words)
            result += f' ({joined_words})'
        if not result:
            result = '---'
        return result

    def __str__(self):
        return self.both

    def clean(self):
        if self.best is not None and self.best not in self.words.all():
            raise ValidationError('Best word must be a standard word for given pair')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Element(models.Model):

    class ElementType(models.IntegerChoices):
        EDGE = 1, 'Edge'
        CORNER = 2, 'Corner'

    faces = models.ManyToManyField(Face)
    type = models.IntegerField(choices=ElementType.choices, null=False, blank=False)

    def __str__(self):
        return ''.join([face.position for face in self.faces.all()])
