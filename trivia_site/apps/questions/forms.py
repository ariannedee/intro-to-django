from django import forms

from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("text", "details")
        widgets = {
            "details": forms.Textarea(attrs={"rows": 3, "class": "textarea"})
        }
