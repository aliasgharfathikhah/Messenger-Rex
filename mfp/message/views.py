from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Q
from .models import Message
from .serializer import MessageSerializer


# Message view
class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Message
from django.contrib.auth.models import User

def message_view(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        text = request.POST['text']
        Message.objects.create(text=text, for_user=user, from_user=request.user)
        return HttpResponseRedirect(f'/messages/{username}')
    else:
        messages = Message.objects.filter(
            Q(from_user=request.user, for_user=user) | 
            Q(from_user=user, for_user=request.user)
        ).order_by('timestamp')
        return render(request, 'html/send_message.html', {'username': username, 'messages': messages})
    
def home(request):
    return render(request, 'html/home.html')

def signup(request):
    return render(request, 'html/signup.html')

def login(request):
    return render(request, 'html/login.html')  