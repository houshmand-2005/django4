from telnetlib import AUTHENTICATION
from unicodedata import name
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render ,redirect,get_object_or_404
from django.db.models import Q
from .models import Room , Topic , Messages
from .forms import RoomForm ,UserForm
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import Articles,roadmaps,films

    
# from django.http import HttpResponse
# Create your views here.
# rooms = [
#     {'id':1,'name':'lerning python'},
#     {'id':2,'name':'lerning c++'},
#     {'id':3,'name':'lerning java'},
# ]
def aboutus(request):
    return render(request, "base/aboutus.html")
def detail(request):
    context = {
        "articles": Articles.objects.filter(status="p"),
        "roadmaps": roadmaps.objects.all(),
        "films": films.objects.all(),
    }
    return render(request, "base/detail.html",context)
def indexhome(request):
    context = {
        "articles": Articles.objects.filter(status="p"),
    }
    return render(request, "base/index.html", context)
    
def loginPage(request):
    Page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'User OR Password does not exist!')

    context = {'Page': Page}
    return render(request, 'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')
def logoutUserRE(request):
    logout(request)
    return redirect('reset_password')
    
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration(plz try different username and password)')

    return render(request, 'base/login_register.html',{'form':form})
    
def home(request):
    q = request.GET.get('q')  if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
    Q(topics__name__icontains=q) |
    Q(name__icontains=q) |
    Q(deprecation__icontains=q)
    # Q(host__user__icontains=q)
    )

    room_count = rooms.count()
    # return render(request, 'home.html',{'rooms':rooms})
    room_messages = Messages.objects.filter(Q(room__topics__name__icontains=q))[:6]
    topics = Topic.objects.all()[:7]
    context = {'rooms':rooms[:6],'topics':topics,
               'room_count':room_count,
               'room_messages':room_messages,
               }
    
    return render(request, 'base/home.html',context)
def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.messages_set.all()
    participants = room.participants.all()
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    if request.method == 'POST':
        message = Messages.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk = room.id)
    context = {'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)
# def login(request):
#     return render(request, 'base/login_register.html')
def userProfile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.messages_set.all()
    topics = Topic.objects.all()[:7]
    context = {'user':user,'rooms':rooms,"room_messages":room_messages,"topics":topics}
    return render(request, 'base/profile.html',context)
@login_required(login_url='login')  
def createroom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic_n, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topics=topic_n,
            name=request.POST.get('name'),
            deprecation=request.POST.get('deprecation')
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        return redirect('home')
    context = {'form':form,'topics':topics}
    return render(request, 'base/room_form.html',context)
@login_required(login_url='login')   
def updateRoom(request,pk):
    room = Room.objects.get(id=pk) 
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        # return HttpResponse("you are not allowed here!!")
        return render(request, 'base/allowed.html')
    context = {'form':form,'topics':topics,'room':room}
    if request.method == 'POST':
        
        topic_name = request.POST.get('topic')
        topic_n, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topics = topic_n
        room.deprecation = request.POST.get('deprecation')
        room.save()
        return redirect('home')
    return render(request, 'base/room_form.html',context)   
@login_required(login_url='login') 
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        # return HttpResponse("you are not allowed here!!")
        return render(request, 'base/allowed.html')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete_room.html',{'obj':room})

#----------------------------------------------------------------
@login_required(login_url='login') 
def deleteMessage(request,pk):
    message = Messages.objects.get(id=pk)
    if request.user != message.user:
        # return HttpResponse("you are not allowed here!!")
        return render(request, 'base/allowed.html')
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete_room.html',{'obj':message})
@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('userProfile',pk=user.id)
    return render(request, 'base/update-user.html',{'form':form})
def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)[:5]
    return render(request, 'base/topics.html', {'topics': topics})
def activatePage(request):
    room_messages =  Messages.objects.all()[:11]
    return render(request, 'base/activity.html',{'room_messages':room_messages})