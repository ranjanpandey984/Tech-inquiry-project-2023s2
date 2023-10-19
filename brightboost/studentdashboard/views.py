from bbapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render

# Create your views here.


@login_required
def studentdashboard(request):
    return render(request, 'studentdashboard/index.html')


# Create your views here.
