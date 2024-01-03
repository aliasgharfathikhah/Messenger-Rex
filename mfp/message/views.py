from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.db.models import Q
from .models import Message
from .form import LoginForm, SignupForm
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
    
    if request.user.is_authenticated:
        messages = Message.objects.filter(from_user=request.user)
        usernames = set([message.for_user.username for message in messages])
        users = User.objects.filter(username__in=usernames)
    else:
        messages = []
        users = []

    username = request.user.username
    return render(request, 'html/home.html', {
        'username': username,
        'users': users
    })

def login(request):
    return render(request, 'html/login.html')  

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            print(form.errors)  # چاپ خطاها
    else:
        form = SignupForm()

    return render(request, 'html/signup.html', {
        'form': form
    })
