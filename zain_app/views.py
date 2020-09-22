from django.shortcuts import render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from django.urls import reverse,reverse_lazy

from .models import Users
# Create your views here.
class UserlistView(ListView):
    template_name='users.html'
    model=Users

class UserkDetailsView(DetailView):
    template_name = 'users_detail.html'
    model = Users

class UserAddView(CreateView):
    template_name='add_new_user.html'
    model=Users
    fields=['title','author','body']

class UserUpdateView(UpdateView):
    template_name='edit_user.html'
    model=Users
    fields=['title','author','body']

class UserDeleteView(DeleteView):
    template_name='user_delete.html'
    model=Users
    success_url= reverse_lazy('users')
