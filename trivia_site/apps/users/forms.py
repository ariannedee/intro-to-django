from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.core.files.images import get_image_dimensions
from django.forms import forms

User = get_user_model()


class UserChangeForm(auth_forms.UserChangeForm):
    password = None

    class Meta(auth_forms.UserChangeForm.Meta):
        model = User
        fields = ("name", "email", "avatar")

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        if not avatar:
            return avatar
        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 1000
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError('Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            max_k = 1000
            if len(avatar) > (max_k * 1024):
                raise forms.ValidationError(
                    f'Avatar file size may not exceed {max_k}k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = User
        fields = ("username", "name", "email",)
