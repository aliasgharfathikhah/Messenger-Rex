from django.shortcuts import render
from rest_framework import viewsets
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
    if request.method == 'POST':
        text = request.POST['text']
        user = get_object_or_404(User, username=username)
        Message.objects.create(text=text, for_user=user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'html/send_message.html', {'username': username})
    