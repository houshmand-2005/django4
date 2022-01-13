from django.shortcuts import render
from .models import Room

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