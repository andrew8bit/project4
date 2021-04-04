from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.login_view, name='login'),
    path('accounts/logout', views.logout_view, name='logout_view'),
    path('accounts/profile/', views.profile_update, name='profile_update'),

    path('bounties/', views.bounties_index, name='bounties'),
    path('bounties/<int:bounty_id>/', views.bounty_show, name='bounties_show'),
    path('bounties/<int:bounty_id>/<int:post_id>/', views.bounty_post, name='bounties_post'),

    path('donation/', views.donation, name="donation"),
    path('charge/', views.charge, name="charge"),
    path('thankyou/<str:args>/', views.thankyouMsg, name="thankyou"),
    path('hoodies/', views.hoodies, name="hoodies"),
    path('tshirt/', views.tshirt, name="tshirt"),
    path('accessories/', views.accessories, name="accessories"),

]
