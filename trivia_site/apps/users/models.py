from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse


class User(AbstractUser):
    """
    Create a custom User class.
    - Not all users have a first and last name, so use a single name field
    - Users should be able to log in with their email, so make it unique
    """
    name = CharField(max_length=255)
    email = models.EmailField('Email address', unique=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)

    USERNAME_FIELD = 'email'                # Log in with email (instead of username)
    REQUIRED_FIELDS = ['name', 'username']  # Require these when creating a superuser

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return settings.STATIC_URL + 'images/avatar.png'
