from django.urls import path

from .views import (
    UserDetailView,
    UserRedirectView,
    UserSignUp,
    UserUpdateView,
    ListView,
)

app_name = "users"
urlpatterns = [
    path("signup/", view=UserSignUp.as_view(), name="signup"),
    path("redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("update/", view=UserUpdateView.as_view(), name="update"),
    path("<str:username>/", view=UserDetailView.as_view(), name="detail"),
    path("me", view=UserDetailView.as_view(), name="my-profile"),
    path("", view=ListView.as_view(), name="list"),
]
