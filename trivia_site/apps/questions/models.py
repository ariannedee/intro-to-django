from django.db import models


class Question(models.Model):
    text = models.CharField('question', max_length=255)
    details = models.TextField(blank=True)
    image = models.ImageField(blank=False)

    def __str__(self):
        return f"Question: {self.text}"

    def __repr__(self):
        return f"Question ({self.pk}): {self.text}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"Choice: {self.text}"

    def __repr__(self):
        return f"Choice ({self.pk}): {self.text}"
