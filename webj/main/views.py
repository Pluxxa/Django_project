# main/views.py

from django.shortcuts import render
from main_1.models import Message

def index(request):
    messages = Message.objects.all()
    return render(request, 'main/index.html', {'messages': messages})
