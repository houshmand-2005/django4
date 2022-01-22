from telnetlib import AUTHENTICATION
from unicodedata import name
from django.contrib import messages
from django.shortcuts import render ,redirect
from django.db.models import Q
from .models import Room , topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

    
# from django.http import HttpResponse
# Create your views here.
# rooms = [
#     {'id':1,'name':'lerning python'},
#     {'id':2,'name':'lerning c++'},
#     {'id':3,'name':'lerning java'},
# ]
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
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

    context = {}
    return render(request, 'base/login_register.html',context)
    

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
    topics = topic.objects.all()
    context = {'rooms':rooms,'topics':topics,'room_count':room_count}
    
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room':room}
    return render(request,'base/room.html',context)
# def login(request):
#     return render(request, 'base/login_register.html')
    
def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'base/room_form.html',context)
    
def updateRoom(request,pk):
    room = Room.objects.get(id=pk) 
    form = RoomForm(instance=room)
    context = {'form':form}
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html',context)   
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete_room.html',{'obj':room})
