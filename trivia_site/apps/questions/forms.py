from django import forms
from django.forms import inlineformset_factory

from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("text", "details")
        widgets = {
            "details": forms.Textarea(attrs={"rows": 3, "class": "textarea"})
        }


# Create a "formset" to update the choices related to a question
# https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/#inline-formsets

ChoiceFormSet = inlineformset_factory(
    parent_model=Question,
    model=Choice,
    fields=('text', 'is_correct', 'details'),
    can_delete=False,
    extra=0,
    min_num=3,
    widgets={
        "text": forms.Textarea(attrs={"rows": 2, "class": "textarea"}),
        "details": forms.Textarea(attrs={"rows": 4, "class": "textarea"}),
    }
)
