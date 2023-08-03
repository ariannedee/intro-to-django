"""
Advanced Django Admin
https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
"""
from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from .forms import UserChangeForm, UserCreationForm

User = get_user_model()  # get the user model as defined by AUTH_USER_MODEL in settings


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """
    Subclass the original UserAdmin
    Uses name field instead of first_name and last name
    Makes email more visible and required during creation
    """
    add_form = UserCreationForm

    # Fieldsets - sections/fields to show in forms (only the change form in this case)
    # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    fieldsets = (("User", {"fields": ("name", "avatar")}),) + tuple(auth_admin.UserAdmin.fieldsets)

    # List display - fields to show in the list display
    list_display = ("username", "email", "name", "is_superuser", "is_staff", "is_active")

    # Search fields - fields to search on in search bar
    search_fields = ("name", "username", "email")

    # List filter - fields to filter on in the right sidebar
    list_filter = ("is_superuser", "is_staff", "is_active",)

    # The original UserAdmin shows a different set of fields when creating a new User
    # Ours requires name and email as well as username and password
    add_fieldsets = (
        (None, {
            "fields": ("username", "name", "email", "password1", "password2", "is_staff")}
         ),
    )

    # Ordering - fields to order by in the list display
    ordering = ("email",)
