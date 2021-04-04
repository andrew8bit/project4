from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponse, HttpResponseRedirect
# bring in some things to make auth easier
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# bring in decorator
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .models import Bounty, Post, Comment
from .forms import PostForm, CommentForm

import stripe
from django.urls import reverse
import os
from django.conf import settings

from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
stripe.api_key = os.getenv('STRIPE_API')

#// ----------------------------
### DONATION//STRIPE FUNCTIONS
#// ----------------------------

def donation(request):
    return render(request, 'donation.html')

def charge(request):

    if request.method == 'POST':
        print('Data:', request.POST)
        amount = int(request.POST['amount'])
        customer = stripe.Customer.create(
            name=request.POST['name'],
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='usd',
            description="Donation"
        )
    return redirect(reverse('thankyou', args=[amount]))

def my_view(request):
    context = {
        'api_key': settings.STRIPE_API
    }
    print(context["api_key"])
    return render('donation.html', context)

def thankyouMsg(request, args):
    amount = args
    return render(request, 'thankyou.html', {'amount': amount}) 

#// ----------------------------
### AUTHORIZATION
#// ----------------------------

## WE PASS THE FUNCTION FROM SIGNUP ANYWHERE WE WANT SIGNUP AND SIGNIN MODAL TO SHOW UP
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ok user created log them in
            login(request, user)
            return redirect('index')
        else:
            error_message = 'That was a no go. Invalid signup'
    # this will run after if it's not a POST or it was invalid
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error_message': error_message
    })

def logout_view(request):
    logout(request)

#// -------------------
### BOUNTIES_PAGES
#// -------------------
@login_required
def bounties_index(request):
    bounties = Bounty.objects.all()
    return render(
        request,
        'bounties_index.html',
        {
        'bounties': bounties
        }
    )

@login_required
def bounty_show(request, bounty_id):
    bounty = Bounty.objects.get(id=bounty_id)
    post_form = PostForm(request.POST or None)
    if request.POST and post_form.is_valid():
        new_post = post_form.save(commit=False)
        new_post.user = request.user
        new_post.bounty = bounty
        new_post.save()
        
        return render(request, 'bounty_show.html', {
        'bounty': bounty,
        'post_form' : post_form
    })

    return render(request, 'bounty_show.html', {
        'bounty': bounty,
        'post_form' : post_form
    })

@login_required
def bounty_post(request, bounty_id, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm(request.POST or None)
    if request.POST and comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.user = request.user
        new_comment.post = post
        new_comment.save()

        return render(request, 'bounty_post.html', {
        'post': post,
        'comment_form': comment_form
    })

    return render(request, 'bounty_post.html', {
        'post': post,
        'comment_form': comment_form
    })

#// -------------------
### SHOP RENDERING
#// -------------------

def hoodies(request):

    return render(request, 'hoodie.html')


def tshirt(request):

    return render(request, 'tshirt.html')


def accessories(request):

    return render(request, 'accessories.html')

#// -------------------
### HOMEPAGE 
#// -------------------

def homepage(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
        # ok user created log them in
            login(request, user)
            return redirect('homepage')

    else:
        error_message = 'That was a no go. Invalid signup'

    login_form = AuthenticationForm

    print(login_form)
    form = UserCreationForm()
    return render(request, 'homepage.html', {
        'login_form': login_form,
        'form': form,
        'error_message': error_message
    })

