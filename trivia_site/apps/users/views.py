from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.decorators.http import require_GET
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView

from .forms import UserCreationForm, UserChangeForm

User = get_user_model()


class UserSignUp(CreateView):
    success_url = reverse_lazy('index')
    template_name = 'users/signup.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, f"Signup success!")
        login(self.request, self.object)
        return response


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_object(self, *args, **kwargs):
        if "username" not in self.kwargs:
            return User.objects.get(username=self.request.user.username)
        else:
            return super().get_object(*args, **kwargs)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Your info was updated")
        return super().form_valid(form)


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("index")


@require_GET
@login_required
def list_view(request):
    if request.user.is_staff:
        users = User.objects.all()
    else:
        users = User.objects.filter(is_staff=False)
    context = {"users": users}
    return render(request, "users/user_list.html", context=context)


class ListView(LoginRequiredMixin, View):  # Same functionality as list_view()
    def get(self, request):
        if request.user.is_staff:
            users = User.objects.all()
        else:
            users = User.objects.filter(is_staff=False)
        context = {"users": users}
        return render(request, "users/user_list.html", context=context)
