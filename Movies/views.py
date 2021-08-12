from django.shortcuts import render , redirect
from .models import MovieDetails , TheaterDetails , SeatBooking
from user.models import AddUser
# Create your views here.



def home(request):
    if request.session.get('email'):
        movies = MovieDetails.objects.all() # Retriving all movies from database
        return render(request , 'home.html' , {'movies': movies})
    else:
        return redirect('/user/signup/')


def selectMovie(request, movie):
    MovieTheater = MovieDetails.objects.get(movieName=movie)
    request.session['movie'] = movie
    theaters = MovieTheater.theaterList.split(',')
    return render (request , 'theater.html' , {'theaters': theaters})


def selectTheater(request,theater):
    TheaterName = TheaterDetails.objects.get(theaterName=theater)
    Screens = []
    if TheaterName.screen_1 == request.session.get('movie'):
        Screens.append('Screen 1')

    if TheaterName.screen_2 == request.session.get('movie'):
        Screens.append('Screen 2')
        
    if TheaterName.screen_3 == request.session.get('movie'):
        Screens.append('Screen 3')
    request.session['theater'] = theater
    return render (request , 'select_screen.html',{'Screens':Screens})


def selectScreen(request , screen):
    request.session['screen'] = screen
    print(screen)
    SeatDetails = SeatBooking.objects.all()
    seat = [i for i in range(1,11)]
    return render(request , 'select_seats.html' , { "SeatDetails":SeatDetails,'Seat':seat }  )
    


def selectSeat(request):
    if request.method == 'POST':
        seat =[ request.POST.get(str(i)) for i in range(1,11)]
        seat = list(filter(None,seat))
        if len(seat)>4:
            error = "Can only book four Tickets"
            SeatDetails = SeatBooking.objects.all()
            seat = [i for i in range(1,11)]
            return render(request , 'select_seats.html' , { "SeatDetails":SeatDetails,'Seat':seat,'error':error } )
        seat =",".join( seat)
        Email = AddUser.objects.get(email= request.session.get('email'))
        TheaterName = TheaterDetails.objects.get(theaterName = request.session.get('theater'))
        screen = request.session.get('screen')
        movie = request.session.get('movie')
        userName = request.session.get('user')
        BookingDetails = {
            "theaterName": TheaterName,
            "userEmail" : Email,
            "userName" : userName,
            "screen" : screen,
            "Seats" : seat,
            "Movie" : movie
        }

        seatDetails = SeatBooking.objects.create(**BookingDetails)
        seatDetails.save()

        del request.session['screen']
        del request.session['movie']
        del request.session['theater']
        return render (request , 'success.html' , {'Seats' : seat} )
    