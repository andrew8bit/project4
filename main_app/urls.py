from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/logout', views.logout_view, name='logout_view'),
    path('bounties/', views.bounties_index, name='bounties'),
    path('bounties/1', views.bounty_show, name='bounties_show'),

    path('donations/', views.donation_view, name="donation_view")

]