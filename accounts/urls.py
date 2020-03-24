from django.urls import path, include
from .views import *


app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('user-edit-profile/', user_edit_profile, name='user_edit_profile'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('change_password/', change_password, name='change_password'),
]

