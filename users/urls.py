from django.contrib.auth.views import LoginView
from django.urls import path, include
from users.forms import UserLoginForm
from .views import RegisterView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(authentication_form=UserLoginForm), name="login"),
    path("logout/", views.logout_user, name="logout1"),
    path("register/", RegisterView.as_view(), name="register"),
    path('', include('django.contrib.auth.urls'))
]









 