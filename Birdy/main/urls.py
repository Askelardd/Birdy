from django.urls import path
from .views import cursos, login_view, index, logout_view, register, uc


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('uc/', uc , name='uc'),
    path('cursos/', cursos , name='cursos'),
]