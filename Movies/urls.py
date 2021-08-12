from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='Home'),
    path('select_movie/<movie>/', views.selectMovie , name='SelectMovie'),
    path('select_theater/<theater>/', views.selectTheater , name='SelectTheater'),
    path('select_screen/<screen>/', views.selectScreen , name='SelectScreen'),
    path('select_seat/', views.selectSeat, name='SelectSeat')
    
    
]