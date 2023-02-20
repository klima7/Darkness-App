import random

from django.db import models
from core.models import Face, Letter


class Element(models.Model):

    class ElementType(models.IntegerChoices):
        EDGE = 1, 'Edge'
        CORNER = 2, 'Corner'

    faces = models.ManyToManyField(Face)
    letters = models.ManyToManyField(Letter)
    type = models.IntegerField(choices=ElementType.choices, null=False, blank=False)

    def __str__(self):
        return ''.join([face.position for face in self.faces.all()])


class ElementWithFace:

    def __init__(self, element):
        self.element = element
        self.face = random.choice(list(self.element.faces.all()))

    @property
    def color(self):
        return self.face.color

    @property
    def other_colors(self):
        return [face.color for face in list(self.element.faces.all()) if face != self.face]

    @property
    def letter(self):
        letter = self.element.letters.filter(face=self.face).first() or '***'
        return letter
