from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import User

# class RegistrationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

