from user.models import AddUser
from django.db import models
# Create your models here.

class MovieDetails(models.Model):
    movieName = models.CharField(max_length=200)
    theaterList = models.TextField()
    movieImage = models.ImageField(upload_to="images/" )

    def __str__(self):
        return self.movieName

class TheaterDetails(models.Model):
    theaterName = models.CharField(primary_key=True,max_length=100)
    screen_1 = models.CharField(max_length=100)
    screen_2 = models.CharField(max_length=100)
    screen_3 = models.CharField(max_length=100)

    def __str__(self):
        return self.theaterName


class SeatBooking(models.Model):
    theaterName = models.ForeignKey(to=TheaterDetails , on_delete=models.CASCADE)
    userEmail = models.ForeignKey( to = AddUser , on_delete = models.CASCADE)
    userName = models.CharField(max_length=50, default = "a")
    screen = models.CharField(max_length = 100)
    Seats = models.CharField(max_length=100)
    Movie = models.CharField(max_length=100)

    def __str__(self):
        return self.userName