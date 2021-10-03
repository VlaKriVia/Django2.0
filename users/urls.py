from django.urls import path

from users.views import login, registration, profile, logout, verify

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<str:activation_key>/', verify, name='verify')
]
