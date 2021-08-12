from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp , name='signup'),
    path('forgotp/', views.forgotPassword , name='ForgotPassword'),
    path('newpass/', views.newPassword , name='newpass'),
    path('login/', views.logIn , name='login'),
    path('logout/', views.logOut , name='logout'),
]
