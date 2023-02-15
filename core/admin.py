from django.contrib import admin
from django import forms

from .models import Pair, Word


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
    list_display = ('both', 'first', 'second')
    search_fields = ('first',)
    inlines = (WordInlineAdmin,)
    form = PairAdminForm


class WordAdmin(admin.ModelAdmin):
    ordering = ('word',)
    search_fields = ('word',)
    list_display = ('word', 'description')


admin.site.register(Pair, PairAdmin)
admin.site.register(Word, WordAdmin)
