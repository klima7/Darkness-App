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
