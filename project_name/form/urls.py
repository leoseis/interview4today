from django.contrib.auth import views as auth_views
from django.urls import path

from . import views                  #importing all views belonging to this app
from .forms import LoginForm          #importing the authethifaction form part

app_name = 'form'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup.html'),
    path('login/', auth_views.LoginView.as_view(template_name='form/login.html', authentication_form=LoginForm), name='login'),
]
