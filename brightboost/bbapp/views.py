from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.get_username() == 'admin':
                return redirect('admindashboard')
            elif user.is_staff:
                return redirect('tutordashboard')
            else:
                return redirect('studentdashboard')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    if request.user.is_authenticated:
        if request.user.is_staff is True:
            return redirect("tutordashboard")
        elif request.user.is_staff is False:
            return redirect("studentdashboard")
        elif (request.user.get_username == "admin"):
            return redirect("admindashboard")
    else:
        return render(request, 'home/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        is_staff = request.POST.get('isstaff', False)
        newuser = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        if is_staff:
            newuser.is_staff = True

        newuser.save()

        # Authenticate and Log the user in
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.get_username() == 'admin':
                return redirect('admindashboard')
            elif user.is_staff:
                return redirect('tutordashboard')
            else:
                return redirect('studentdashboard')
                # return render(request, 'studentdashboard/index.html')

        # messages.success(request, 'You are registered successfully. ')
        return redirect('signup')

    return render(request, 'home/signup.html')


def user_logout(request):
    logout(request)
    return redirect('login')
