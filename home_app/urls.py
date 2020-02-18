from django.urls import path
from .views import homePage, postDetail

app_name="home_app"

urlpatterns = [
    path('post_detail/<int:pk>/', postDetail, name='post_detail'),
    path('', homePage, name='index'),
]
