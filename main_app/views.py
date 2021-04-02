from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.http import HttpResponse, HttpResponseRedirect
# bring in some things to make auth easier
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# bring in decorator
from django.contrib.auth.decorators import login_required

from django.forms.models import model_to_dict

import stripe
from django.urls import reverse
import os
from django.conf import settings
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
stripe.api_key = os.getenv('STRIPE_API')


def my_view(request):
    context = {
        'api_key': settings.STRIPE_API
    }
    print(context["api_key"])
    return render('donation.html', context)

# SIGNUP


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


# HOMEPAGE
def index(request):
    # WE ARE GOING TO CHANGE THIS WHEN WE CREATE OUR OWN USER MODEL AND FORM
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

    login_form = AuthenticationForm

    print(login_form)
    form = UserCreationForm()
    return render(request, 'index.html', {
        'login_form': login_form,
        'form': form,
        'error_message': error_message
    })


def logout_view(request):
    logout(request)


def donation(request):
    return render(request, 'donation.html')

 # my_stripe= os.environ.get("MY_STRIPE")
 # print(my_stripe)


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

# BOUNTIES_INDEX


def bounties_index(request):

    return render(request, 'bounties_index.html')


def bounty_show(request):

    return render(request, 'bounty_show.html')


def thankyouMsg(request, args):
    amount = args
    return render(request, 'thankyou.html', {'amount': amount})


def shop(request):

    return render(request, 'shop.html')
