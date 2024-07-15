# main_1/views.py

from django.shortcuts import render, redirect
from .models import Message

def new(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        x_position = request.POST.get('x_position')
        y_position = request.POST.get('y_position')
        if text and x_position and y_position:
            message = Message(text=text, x_position=x_position, y_position=y_position)
            message.save()
            return redirect('index')
    return render(request, 'new.html')

def index(request):
    messages = Message.objects.all()
    return render(request, 'index.html', {'messages': messages})
