from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
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
