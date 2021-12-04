from django.forms import ModelForm
from .models import User, Room

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'