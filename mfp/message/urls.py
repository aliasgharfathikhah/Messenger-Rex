from django.urls import path
from rest_framework import routers
from . import views
from .views import MessageViewset

router = routers.DefaultRouter()
router.register('', MessageViewset)

urlpatterns = [
    path('messages/<str:username>/', views.message_view, name='message_view'),
    
]

urlpatterns += router.urls