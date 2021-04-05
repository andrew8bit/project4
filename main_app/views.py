from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# bring in some things to make auth easier
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, password_validation
# bring in decorator
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .models import Bounty, Post, Comment
from .forms import PostForm, CommentForm, UserForm, DeleteUserForm

import stripe
from django.urls import reverse
import os
from django.conf import settings

from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
stripe.api_key = os.getenv('STRIPE_API')

# // ----------------------------
# DONATION//STRIPE FUNCTIONS
# // ----------------------------


def donation(request):
    return render(request, 'donation/donation.html')


def charge(request):

    if request.method == 'POST':
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
    return render('donation/donation.html', context)


def thankyouMsg(request, args):
    amount = args
    return render(request, 'donation/thankyou.html', {'amount': amount})

# // ----------------------------
# AUTHORIZATION
# // ----------------------------

# WE PASS THE FUNCTION FROM SIGNUP ANYWHERE WE WANT SIGNUP AND SIGNIN MODAL TO SHOW UP


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ok user created log them in
            login(request, user)
            messages.success(request, 'Sign Up was successful, welcome!')
            return redirect('/')
        else:
            messages.error(request, 'Unsuccessful Sign up')
    # this will run after if it's not a POST or it was invalid
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })


def login_view(request):
    messages.success(request, 'Login Successful')
    login(request, user)


def logout_view(request):
    messages.success(request, 'Logout Successful')
    logout(request)


@login_required
def profile_update(request):
    user = User.objects.get(id=request.user.id)
    password_form = PasswordChangeForm(user=request.user, data=request.POST)
    username_form = UserForm(initial=model_to_dict(user), data=request.POST)
    delete_form = DeleteUserForm(data=request.POST)

    if request.method == 'POST':
        if username_form.is_valid():
            user.username = request.POST.get('username')
            messages.success(request, f"Changed username to {user.username} ")
            user.save()

        if password_form.is_valid():
            password_form.save()
            messages.success(request, "Successfully Changed Password")
            update_session_auth_hash(request, password_form.user)

        if delete_form.is_valid():
            confirmed = user.check_password(request.POST.get('password'))
            if confirmed:
                user.is_active = False
                messages.error(request, "User has been deleted")
                user.save()
            if not confirmed:
                messages.error(request, "Password was not confirmed")

        return redirect('/accounts/profile/')

    return render(request, 'registration/profile.html', {
        'password_form': password_form,
        'username_form': username_form,
        'delete_form': delete_form

    })

# // -------------------
# BOUNTIES_PAGES
# // -------------------


@login_required
def bounties_index(request):
    bounties = Bounty.objects.all()
    return render(
        request,
        'bounties/bounties_index.html',
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
        messages.success(request, 'New Post Was Created!')
        new_post.save()

        return render(request, 'bounties/bounty_show.html', {
            'bounty': bounty,
            'post_form': post_form
        })

    return render(request, 'bounties/bounty_show.html', {
        'bounty': bounty,
        'post_form': post_form
    })


@login_required
def bounty_post(request, bounty_id, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm(request.POST or None)
    if request.POST and comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.user = request.user
        new_comment.post = post
        messages.success(request, 'Comment was added!')
        new_comment.save()

        return render(request, 'bounties/bounty_post.html', {
            'post': post,
            'comment_form': comment_form
        })

    return render(request, 'bounties/bounty_post.html', {
        'post': post,
        'comment_form': comment_form
    })

# // -------------------
# SHOP RENDERING
# // -------------------


def hoodies(request):

    return render(request, 'shop/hoodie.html')


def tshirt(request):

    return render(request, 'shop/tshirt.html')


def accessories(request):

    return render(request, 'shop/accessories.html')

# // -------------------
# HOMEPAGE
# // -------------------

    return render(request, 'bounty_post.html')


def educate(request):

    return render(request, 'educate.html')


def reclaim(request):

    return render(request, 'reclaim.html')


def team(request):

    return render(request, 'team.html')


def homepage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
        # ok user created log them in
            login(request, user)
            return redirect('homepage')
        else:
            messages.success(request, 'Sign Up was successful, welcome!')

    login_form = AuthenticationForm

    form = UserCreationForm()
    return render(request, 'homepage.html', {
        'login_form': login_form,
        'form': form,
    })
