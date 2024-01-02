from django.urls import path
from rest_framework import routers
from . import views
from .views import MessageViewset
from django.contrib.auth import views as auth_views
from .form import LoginForm

router = routers.DefaultRouter()
# router.register('', MessageViewset)

urlpatterns = [
    path('', views.home, name='home'),
    path('messages/<str:username>/', views.message_view, name='message_view'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='html/login.html', authentication_form=LoginForm), name='login'),
    
]

urlpatterns += router.urls