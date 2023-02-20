from django.contrib import admin
from .models import Element


class ElementAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'type')


admin.site.register(Element, ElementAdmin)