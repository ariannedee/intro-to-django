from django.contrib import admin
from django.utils.html import format_html

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

    list_display = ('pk', 'text', 'choice_list')
    list_display_links = ('text',)

    def choice_list(self, obj):
        choices = []
        for choice in obj.choices.all():
            if choice.is_correct:
                choices.append(f"<strong>{choice.text}</strong>")
            else:
                choices.append(choice.text)
        return format_html('<br>'.join(choices))

    choice_list.short_description = "Choices"
