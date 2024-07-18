from django.urls import path
from .views.home import home
from .views.signup import signup
from .views.login import login


# 
urlpatterns = [
    path("",home.as_View()), 
    path("signup",signup.as_View(),name='signup'),
    path("login",login.as_View(),name='login')
]

