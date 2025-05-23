from django.contrib import admin
from django import forms

from .models import Pair, Word, Letter, Face, Color


class PairAdminForm(forms.ModelForm):
    class Meta:
        model = Pair
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PairAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['best'].queryset = self.instance.words


class WordInlineAdmin(admin.TabularInline):
    model = Word
    fields = ('word', 'description')
    extra = 0
    show_change_link = True


class PairAdmin(admin.ModelAdmin):
    ordering = ('first', 'second')
    list_display = ('__str__', 'best', 'description', 'difficult', 'other')
    readonly_fields = ('first', 'second')
    list_filter = ('difficult', 'first', 'second', ('best', admin.EmptyFieldListFilter))
    search_fields = ('',)
    inlines = (WordInlineAdmin,)
    form = PairAdminForm
    actions = ['set_difficult_to_false', 'set_difficult_to_true']

    def other(self, pair):
        return ', '.join([word.word for word in pair.words.all() if word != pair.best])

    def description(self, pair):
        return pair.best.description if pair.best else None

    def get_search_results(self, request, queryset, search_term):
        if len(search_term) == 0:
            return queryset, False
        elif len(search_term) == 1:
            return queryset.filter(first__char=search_term), False
        elif len(search_term) == 2:
            return queryset.filter(first__char=search_term[0], second__char=search_term[1]), False
        return Pair.objects.none(), False
    
    def set_difficult_to_false(self, request, queryset):
        queryset.update(difficult=False)
    set_difficult_to_false.short_description = 'Set difficult to false'
    
    def set_difficult_to_true(self, request, queryset):
        queryset.update(difficult=True)
    set_difficult_to_true.short_description = 'Set difficult to true'


class WordAdmin(admin.ModelAdmin):
    ordering = ('word',)
    search_fields = ('word',)
    list_display = ('word', 'pair', 'description')


class LetterAdmin(admin.ModelAdmin):
    ordering = ('char',)
    list_display = ('__str__', 'face')
    list_filter = ('face',)


class FaceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'color')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'red', 'green', 'blue')


admin.site.register(Pair, PairAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Letter, LetterAdmin)
admin.site.register(Face, FaceAdmin)
admin.site.register(Color, ColorAdmin)
