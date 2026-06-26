from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        field_config = {
            "username": {
                "placeholder": "Choose a username",
                "autocomplete": "username",
            },
            "email": {
                "placeholder": "you@example.com",
                "autocomplete": "email",
            },
            "password1": {
                "placeholder": "Create a password",
                "autocomplete": "new-password",
            },
            "password2": {
                "placeholder": "Confirm your password",
                "autocomplete": "new-password",
            },
        }

        for name, attrs in field_config.items():
            self.fields[name].widget.attrs.update({
                "class": "register-input",
                **attrs,
            })


class LoginForm(AuthenticationForm):
    pass
