from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#####  Will have unique username & email  #####
class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    about_me = models.TextField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Room(models.Model):

    host =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
