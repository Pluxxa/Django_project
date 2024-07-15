# main_1/views.py

from django.shortcuts import render, redirect
from .models import Message

def index(request):
    messages = Message.objects.all()
    return render(request, 'main/index.html', {'messages': messages})

def new(request):
    if request.method == "POST":
        text = request.POST['text']
        x_position = request.POST['x_position']
        y_position = request.POST['y_position']
        Message.objects.create(text=text, x_position=x_position, y_position=y_position)
        return redirect('index')
    return render(request, 'main_1/new.html')
