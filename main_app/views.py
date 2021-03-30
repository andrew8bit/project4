from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.http import HttpResponse, HttpResponseRedirect
# bring in some things to make auth easier 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# bring in decorator
from django.contrib.auth.decorators import login_required

from django.forms.models import model_to_dict

def index(request):
    return render(request, 'index.html')