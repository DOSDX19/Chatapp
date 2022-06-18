from dataclasses import field
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView , UpdateView , FormView
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.views import LoginView
from .models import User
from django.contrib.auth import authenticate , login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Message

from .forms import MessageForm, RegisterForm
# Create your views here.

class Login(LoginView):
    template_name = 'chat/index.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("chat")

   
class Register(FormView):
    template_name = 'chat/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('chat')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('chat')
        return super(Register, self).get(*args, **kwargs)




class Chat(View , LoginRequiredMixin):

    def get(self,request):
        form = MessageForm()
        return render(request , "chat/chat.html" , {
            "messages":Message.objects.all(),
            "form" : form
        })

    
    def post(self , request ):
        message_form = MessageForm(request.POST)
        username= request.POST["secret"]
        print(username)
        text = request.POST["text"]
        print(text)
        message = Message(username=username, text = text)
        message.save()
        return HttpResponseRedirect(reverse("chat"))
