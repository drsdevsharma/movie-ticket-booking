from django.shortcuts import render, redirect
from .models import AddUser # User model that store all info related to user
from django.contrib.auth import hashers # For storing passwords in hash format
from django.contrib import messages


# Create your views here.


def signUp (request):
    if request.method == 'POST': # Handling post request
        email = request.POST.get('email')
        try:
            newUser = AddUser.objects.get(email=email) # Check if user already exists
        except AddUser.DoesNotExist as e: # User does not exists
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            if cpassword == password: # checks if password are matching
                firstName = request.POST.get('firstName')
                lastName = request.POST.get('lastName')
                phoneNumber = request.POST.get('phoneNumber')
                userData = { # creating user data dictionary
                    'firstName': firstName,
                    'lastName': lastName,
                    'phoneNumber': phoneNumber,
                    'email' : email,
                    'password' :hashers.make_password(password) # Hashing Password
                }
                newUser = AddUser.objects.create(**userData) # creating a new user
                newUser.save()
                request.session['user'] = firstName + ' ' + lastName 
                request.session['email'] = email
                return redirect('/')
            else:
                Error = "Password not matching !!!"
                return render (request, 'signup.html', {'error': Error}) # if not then sending back to signup page

        else:
            Error = " User already exists ...."
            return render (request, 'login.html', {'error': Error}) # if user exists then sending back to login page
    else:
        return render (request, 'signup.html') # Handling get request


def logIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            newUser = AddUser.objects.get(email=email)
        except AddUser.DoesNotExist as e:
            Error = " User does not exist !!!"
            return render (request, 'signup.html', {'error': Error}) # if user exists then sending back to signup page
        else:
            password = request.POST.get ('password')
            verify_password = hashers.check_password(password , newUser.password)
            if verify_password :
                request.session['email'] = email
                request.session['user'] = newUser.firstName + ' ' +newUser.lastName 
                print(request.session.get('user'))

                return redirect ('/')
            else:
                Error = "Wrong credentials ...."
                return render(request, 'login.html', {'error':Error})
    else:
        return render (request, 'login.html')


def logOut(request):
    del request.session['email']
    return redirect ('/user/login/')


def forgotPassword(request):
    if request.method == 'POST':
        phoneNumber = request.POST.get('phoneNumber')
        try:
            userData = AddUser.objects.get(phoneNumber=phoneNumber)
        except AddUser.DoesNotExist as e:
            messages.error(request , "User does not exist !!!"   )
            return redirect('/user/forgotp/')
        else:
            request.session['user'] = userData.phoneNumber
            print(userData.phoneNumber)
            return render(request , 'newpassword.html')
            
    else:
        return render (request, 'forgetpassword.html')


def newPassword(request):
    if request.method == 'POST':
        password = request.POST.get ('password')
        cpassword = request.POST.get ('cpassword')
        if cpassword == password:
            password = hashers.make_password(password)
            if request.session.get('user'):
                userData = AddUser.objects.get (phoneNumber = request.session.get('user'))
                userData.password = password
                userData.save()
                return redirect ('/user/login/')
            else:
                return render (request, 'newpassword.html')
        else:
            Error = "Password not matching !!!"
            return render (request, 'newpassword.html', {'error': Error}) 
    else:
        return render (request, 'newpassword.html')
    
        
