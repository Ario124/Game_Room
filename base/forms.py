from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Room


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'