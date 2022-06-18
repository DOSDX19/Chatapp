from django.urls import path 
from . import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("" , views.Login.as_view() , name="login"),
    path("register", views.Register.as_view() , name="register"),
    path("chat", views.Chat.as_view() , name = "chat"),
    path('logout', LogoutView.as_view(next_page="login") , name= 'logout' ),
    
]
