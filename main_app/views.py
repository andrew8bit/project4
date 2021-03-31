from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.http import HttpResponse, HttpResponseRedirect
# bring in some things to make auth easier 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
# bring in decorator
from django.contrib.auth.decorators import login_required

from django.forms.models import model_to_dict

def index(request):
    return render(request, 'index.html')

# SIGNUP 
def signup(request): 
  error_message= ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # ok user created log them in
      login(request, user)
      return redirect('index')
    else:
      error_message='That was a no go. Invalid signup'
  # this will run after if it's not a POST or it was invalid
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form, 
    'error_message': error_message
  })

def logout_view(request):
    logout(request)
