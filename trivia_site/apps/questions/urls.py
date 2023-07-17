from django.urls import path

from .views import (
    answer_view,
    complete,
    question_view,
    question_update,
    next_question,
    new_game,
)

app_name = "questions"
urlpatterns = [
    path("new/", view=new_game, name="new"),
    path("complete/", view=complete, name="complete"),
    path("question/", view=next_question, name="question"),
    path("question/<int:pk>/", view=question_view, name="question"),
    path("question/<int:pk>/update/", view=question_update, name="update"),
    path("question/<int:question_pk>/choice/<int:choice_pk>", view=answer_view, name="answer"),
]
