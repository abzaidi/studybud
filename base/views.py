from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
# rooms = [
#     {'id': 1, 'name': 'Help me solve transportation problems'},
#     {'id': 2, 'name': 'looking for fellow javascript learner'},
#     {'id': 3, 'name': 'lets learn algorithms together'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
