import re
from django.shortcuts import render ,redirect
from .models import Room
from .forms import RoomForm

# from django.http import HttpResponse
# Create your views here.
# rooms = [
#     {'id':1,'name':'lerning python'},
#     {'id':2,'name':'lerning c++'},
#     {'id':3,'name':'lerning java'},
# ]

def home(request):
    rooms = Room.objects.all()
    # return render(request, 'home.html',{'rooms':rooms})
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'room':room}
    return render(request,'base/room.html',context)
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
    