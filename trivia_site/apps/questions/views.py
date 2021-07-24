import random

from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from .forms import QuestionForm
from .models import Question, Choice


def random_question(request):
    question_ids = [q.pk for q in Question.objects.all()]
    pk = random.choice(question_ids)
    return redirect('questions:question', pk=pk)


def question_view(request, pk):
    q = get_object_or_404(Question, pk=pk)
    context = {"question": q}
    return render(request, "questions/question.html", context=context)


def question_update(request, pk):
    q = get_object_or_404(Question, pk=pk)
    ChoiceFormSet = inlineformset_factory(
        Question, Choice, fields=('text', 'is_correct'), can_delete=False, extra=0
    )
    if request.method == 'POST':
        formset = ChoiceFormSet(request.POST, instance=q)
        form = QuestionForm(request.POST, instance=q)
        if formset.is_valid() and form.is_valid():
            formset.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, "This question was updated")
        return redirect(q.get_absolute_url())
    else:
        formset = ChoiceFormSet(instance=q)
        form = QuestionForm(instance=q)

    context = {"question": form.instance, 'form': form, 'formset': formset}
    return render(request, "questions/question_edit.html", context=context)


def question_view_no_shortcuts(request, pk):
    # instead of get_object_or_404()
    try:
        q = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404('No Question matches the given query.')

    context = {"question": q}

    # instead of render()
    content = loader.render_to_string("questions/question.html", context, request)
    return HttpResponse(content, content_type="text/html", status=200)


def answer_view(request, question_pk, choice_pk):
    q = get_object_or_404(Question, pk=question_pk)
    c = get_object_or_404(Choice, question=q, pk=choice_pk)
    context = {"question": q, "selected_choice": c}
    return render(request, "questions/answer.html", context=context)
