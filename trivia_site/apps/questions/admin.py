from django.contrib import admin
from django.utils.html import format_html

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):  # Create/edit related objects in a table
    model = Choice
    min_num = 2     # Minimum number of related objects
    extra = 0       # How many extra rows to show


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

    list_display = ('pk', 'text', 'choice_list', 'difficulty')
    list_display_links = ('text',)

    def choice_list(self, obj):                   # Custom field for list_display
        choices = []
        for choice in obj.choices.all():
            text = choice.text.replace('{', '{{').replace('}', '}}')
            if choice.is_correct:
                choices.append(f"<strong>{text}</strong>")
            else:
                choices.append(text)
        return format_html('<br>'.join(choices))  # Allow HTML

    choice_list.short_description = "Choices"     # Set header name for custom field
