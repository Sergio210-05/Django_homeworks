from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            row = form.cleaned_data
            if row.get('is_main'):
                count += 1
            if count == 0:
                raise ValidationError('Укажите основной раздел')
            elif count > 1:
                raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
