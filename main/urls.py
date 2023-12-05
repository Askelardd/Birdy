from django.urls import path
from . import views
from .views import login_view, index, logout_view, register


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]