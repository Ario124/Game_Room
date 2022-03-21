from django.db.models import expressions
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import User, Room, Topic, Message, State
from .forms import RoomForm, UserRegisterForm, UserAvatarForm
from django.core.paginator import Paginator

# Create your views here.




def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )


    room_pages = Paginator(rooms, 4)
    page_number = request.GET.get('page')
    page = room_pages.get_page(page_number)

    genre = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))[0:3]

    context = {'rooms': rooms, 'genre': genre,
                'room_count': room_count, 'room_messages': room_messages, 'page': page}
    return render(request, 'base/home.html', context)

def room(request, pk):
    page = 'room'
    genre = Topic.objects.all()
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-created')[0:3]
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'page': page, 'room':room, 'room_messages': room_messages, 'participants': participants, 'genre': genre}

    return render(request, 'base/room.html', context)

def loginPage(request):
    page = 'login'
    
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    genre = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page, 'genre': genre, 'room_messages': room_messages}
    return render(request, 'base/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    genre = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form, 'genre': genre, 'room_messages': room_messages}
    return render(request, 'base/login.html', context)



def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_message = user.message_set.all()
    genre = Topic.objects.all()

    room_message = Message.objects.filter()[0:3]
    total_messages = Message.objects.all()
    context = {'user': user, 'rooms':rooms, 'room_message':room_message, 'genre':genre, 'total_messages': total_messages}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def createRoom(request):
    genre = Topic.objects.all()
    state = State.objects.all()
    room_messages = Message.objects.all()[0:3]

    if request.method == 'POST':

        state_name = request.POST['state']
        state = State.objects.get(name=state_name)

        genre_name = request.POST.get('genre')
        genre = Topic.objects.get(name=genre_name)


        Room.objects.create(
            host = request.user,
            topic = genre,
            state = state,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )


        return redirect('home')


    context = {'genre': genre, 'state': state, 'room_messages': room_messages}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    genre = Topic.objects.all()
    state = State.objects.all()
    room_messages = Message.objects.all()[0:3]

    if request.user != room.host:
        return HttpResponse('You are not allowed here.')

    if request.method == 'POST':

        state_name = request.POST['state']
        state = State.objects.get(name=state_name)

        genre_name = request.POST.get('genre')
        genre = Topic.objects.get(name=genre_name)

        room.state = state
        room.topic = genre
        room.name = request.POST.get('name')
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'genre': genre, 'room': room, 'state':state, 'room_messages': room_messages}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    page = 'delete-room'
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    genre = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed here.')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj': room, 'genre': genre, 'room_messages': room_messages, 'page': page}
    return render(request, 'base/delete.html', context)


@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed here.')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})


@login_required(login_url='login')
def updateProfile(request, pk):
    about_me = User.objects.all()
    user = User.objects.get(id=pk)
    avatar = User.objects.all()
    form = UserAvatarForm(instance=user)
    genre = Topic.objects.all()

    if request.method == 'POST':
        form = UserAvatarForm(request.POST, request.FILES, instance=user)
        about_me = request.POST.get('about_me')
        avatar = form
        user.about_me = about_me
        user.avatar = avatar
        form.save()
        user.save()

        return redirect('home')

    context = {'about_me': about_me, 'avatar':avatar, 'form': form, 'genre': genre}
    return render(request, 'base/update_profile.html', context)