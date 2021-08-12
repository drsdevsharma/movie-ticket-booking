from django.contrib import admin
from .models import MovieDetails,TheaterDetails,SeatBooking


# Register your models here.

admin.site.register(MovieDetails)
admin.site.register(TheaterDetails)
admin.site.register(SeatBooking)