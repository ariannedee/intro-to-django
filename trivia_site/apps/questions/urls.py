from django.urls import path

from .views import (
    answer_view,
    question_view,
    question_update,
    random_question,
)

app_name = "questions"
urlpatterns = [
    path("question/", view=random_question, name="question"),
    path("question/<int:pk>/", view=question_view, name="question"),
    path("question/<int:pk>/update/", view=question_update, name="update"),
    path("question/<int:question_pk>/choice/<int:choice_pk>", view=answer_view, name="answer"),
]
