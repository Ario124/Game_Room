from django.db.models import expressions
from django.contrib import messages
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import User

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def room(request):
    return render(request, 'base/room.html')

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('room')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('room')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'base/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')