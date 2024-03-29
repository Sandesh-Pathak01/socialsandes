from django.urls import path
from . import views

urlpatterns = [
    path('loginpage', views.login_page, name='login_page'),
    path('signuppage', views.signup_page, name='signup_page'),
    path('logout/', views.logout_user, name='logout'),
]