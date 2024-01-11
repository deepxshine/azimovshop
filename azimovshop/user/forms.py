from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User # что заполняем ?
        fields = ('first_name', 'last_name', 'username', 'email') # чем заполняем