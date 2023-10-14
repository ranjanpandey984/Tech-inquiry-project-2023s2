from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def admindashboard(request):
    students = User.objects.filter(is_staff=False).count()
    teachers = User.objects.filter(is_staff=True).count()
    context = {
        "students": students,
        "teachers": teachers
    }
    return render(request, 'admindashboard/index.html', context)


def teacher(request):
    teachers = User.objects.filter(is_staff=True).exclude(
        username="admin").exclude(is_superuser=True)
    context = {
        "teachers": teachers
    }
    return render(request, 'admindashboard/teacher/index.html', context)


def addTeacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        is_staff = True
        newuser = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff
        )
        newuser.save()
        messages.success(request, "Teacher Added Successfully")
        return redirect('teacher')

    return render(request, 'admindashboard/teacher/add.html')


def editTeacher(request, id):
    teacher = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        teacher.username = username
        teacher.first_name = first_name
        teacher.email = email
        teacher.last_name = last_name

        teacher.save()
        messages.success(request, "Teacher Edited Successfully")
        return redirect('teacher')
    context = {
        'teacher': teacher
    }
    return render(request, 'admindashboard/teacher/edit.html', context)


def deleteTeacher(request, id):
    teacher = User.objects.get(id=id)
    teacher.delete()
    messages.info(request, "Teacher Deleted Successfully")
    return redirect('teacher')
