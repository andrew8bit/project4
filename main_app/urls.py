from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('accounts/signup', views.signup, name='signup'),
    path('accounts/logout', views.logout_view, name='logout_view'),

    path('bounties/', views.bounties_index, name='bounties'),
    # REPLACE #1 WITH ID
    path('bounties/1', views.bounty_show, name='bounties_show'),
    path('bounties/1/1', views.bounty_post, name='bounties_post'),

    path('donation/', views.donation, name="donation"),
    path('charge/', views.charge, name="charge"),
    path('thankyou/<str:args>/', views.thankyouMsg, name="thankyou"),
    path('hoodies/', views.hoodies, name="hoodies"),
    path('tshirt/', views.tshirt, name="tshirt"),
    path('accessories/', views.accessories, name="accessories"),
    path('educate/', views.educate, name="educate"),
    path('recover/', views.recover, name="recover"),
    path('team/', views.team, name="team"),
]
