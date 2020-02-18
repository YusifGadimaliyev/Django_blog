from django.urls import path, include
from .views import *


app_name = "accounts"

urlpatterns = [
    path('profile/', profile, name="profile"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]

