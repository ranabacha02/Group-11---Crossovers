from io import StringIO
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required #to restrict certain funcs
from django.db.models import Q #for search filter
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from .models import Room, Topic, Message, Fan #import model we want to query
from .forms import RoomForm #import the form for Room
# Create your views here.



#rooms = [
 #   {'id':1, 'name':'lets learn pyton'},
   # {'id':2, 'name':'design with me'}, 
  #  {'id':3, 'name':'frontend developers'},

#]

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:   #if already logged in
        return redirect('home')


    if request.method == 'POST':    #aka when the user submits user & pass
        username = request.POST.get('username').lower()     #gets the username inserted by user
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username) #checks if user exist
        except:
            messages.error(request, 'User does not exist') #throws in an error msg if user doesnt exist

        user = authenticate(request, username=username, password=password) #authenticates user
        if user is not None:
            login(request, user)    #if correct credentials, login user (create new session)
            return redirect('home')
        else: 
            messages.error(request, 'Username OR Password does not exist')
    context={'page': page}
    return render(request, 'base1/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()   #uses a Django created form for createing user
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #form is saved and to directly access user put commit false
            user.username = user.username.lower() #make sure username is lowercase
            user.save()
            login(request, user)    #logs in user
            if request.POST.get('fav_language') == "FAN":
                fan = Fan.objects.create(
                    user = request.user,
                    name = request.user.username
                   )
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'base1/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q')  if request.GET.get('q') != None else ''  #q is same as in home.html file
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) | 
        Q(name__icontains=q) |          #this allows searching by topic, name or desc
        Q(description__icontains=q)
    )
    topics = Topic.objects.all() #lists all topics in homepage
    room_count = rooms.count()    #count how many rooms 
    fans = Fan.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains = q)) #displays msgs


    context = {'rooms': rooms, 'topics':topics, 'room_count': room_count, 'room_messages': room_messages, 'fans':fans}
    return render(request, 'base1/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)  #return a specific room item defined by id
    room_messages = room.message_set.all().order_by('-created') #we can query child obj (msgs) of a specific room. set.all is give us all msgs 
    room.participants.add(room.host) #adds the host as participant too
    participants= room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create( #creates actual msg
            user=request.user,  #the user who makes the req
            room=room,          
            body=request.POST.get('body') #whtvr its name in room.html, pass it(this is the body we pass when we writr the comment)
        )
        room.participants.add(request.user)     #to add participant
        return redirect('room', pk) #redirect to this specific room

    
    context = {'room': room, 'room_messages' : room_messages, 'participants': participants}   #orders by descednign order
    return render(request, 'base1/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()  #brings all rooms for that user
    room_messages = user.message_set.all()  #brings all msgs user sent
    topics= Topic.objects.all()

    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'base1/profile.html', context)


def history(request):
    page = 'history'
    return render(request, 'base1/history_values.html', {'page': page})
def values(request):
    page ='values'
    return render(request, 'base1/history_values.html', {'page': page})
def news(request):
    return render(request, 'base1/news_home.html', {})

@login_required(login_url='login')     #createRoom func limited to logged in users
def createRoom(request):                     #it redirects to login page
    form = RoomForm()
   
    if request.method == 'POST':    #if post action done
        form = RoomForm(request.POST) #add data to form
        if form.is_valid():
            form.save()             #save form in databse
            return redirect('home') #returns user to homepage
    context={'form': form}
    return render(request, 'base1/room.form.html', context)

@login_required(login_url='login') 
def updateRoom(request,pk):         #pk is to know what room we're updating
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)  #form is pre-filled with Room instance
    
    if request.user != room.host: #not allowed to update if ur not host of room
        return HttpResponse("you are not allowed to update")

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={'form': form}
    return render(request, 'base1/room.form.html', context)

@login_required(login_url='login') 
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host: #not allowed to update if ur not host of room
        return HttpResponse("you are not allowed to update")

    if request.method == 'POST':
        room.delete()           #item deleted from database
        return redirect('home')
    return render(request, 'base1/delete.html',{'obj':room}) #we call room obj

@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user: #not allowed to update if ur not host of room
        return HttpResponse("you are not allowed to update")

    if request.method == 'POST':
        message.delete()           #item deleted from database
        return redirect('home')
    return render(request, 'base1/delete.html',{'obj':message})
