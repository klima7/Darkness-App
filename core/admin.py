from django.contrib import admin

from .models import Pair, Word


class WordInlineAdmin(admin.TabularInline):
    model = Word
    fields = ('word', 'best', 'description')
    extra = 0
    show_change_link = True


class PairAdmin(admin.ModelAdmin):
    ordering = ('first', 'second')
    list_display = ('both', 'first', 'second')
    search_fields = ('first',)
    inlines = (WordInlineAdmin,)


class WordAdmin(admin.ModelAdmin):
    ordering = ('word',)
    search_fields = ('word',)
    list_display = ('word', 'description', 'best')
    list_filter = ('best',)


admin.site.register(Pair, PairAdmin)
admin.site.register(Word, WordAdmin)
