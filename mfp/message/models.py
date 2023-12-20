from django.db import models
from django.contrib.auth.models import User

# Model for message
class Message(models.Model):
    text = models.TextField()
    for_user = models.ForeignKey(User, on_delete=models.CASCADE)