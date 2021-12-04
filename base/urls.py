from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),

    path('create-room/', views.createRoom, name="create-room"),
]