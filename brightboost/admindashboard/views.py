from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def admindashboard(request):
    students = User.objects.filter(is_staff=False).count()
    teachers = User.objects.filter(is_staff=True).count()
    context = {
        "students": students,
        "teachers": teachers
    }
    return render(request, 'admindashboard/index.html', context)
