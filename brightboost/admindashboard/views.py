from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bbapp.models import *

# Create your views here.


@login_required
def admindashboard(request):
    students = User.objects.filter(is_staff=False).exclude(
        username="admin").exclude(is_superuser=True).count()
    teachers = User.objects.filter(is_staff=True).exclude(
        username="admin").exclude(is_superuser=True).count()
    sessions = Session.objects.count()
    questions = Question.objects.count()
    context = {
        "students": students,
        "teachers": teachers,
        "sessions": sessions,
        "questions": questions
    }
    return render(request, 'admindashboard/index.html', context)


@login_required
def teacher(request):
    teachers = User.objects.filter(is_staff=True).exclude(
        username="admin").exclude(is_superuser=True)
    context = {
        "teachers": teachers
    }
    return render(request, 'admindashboard/teacher/index.html', context)


@login_required
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


@login_required
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


@login_required
def deleteTeacher(request, id):
    teacher = User.objects.get(id=id)
    teacher.delete()
    messages.info(request, "Teacher Deleted Successfully")
    return redirect('teacher')


@login_required
def student(request):
    students = User.objects.filter(is_staff=False).exclude(
        username="admin").exclude(is_superuser=True)
    context = {
        "students": students
    }
    return render(request, 'admindashboard/student/index.html', context)


@login_required
def addStudent(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['password']
        is_staff = False
        newuser = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff
        )
        newuser.save()
        messages.success(request, "Student Added Successfully")
        return redirect('student')

    return render(request, 'admindashboard/student/add.html')


@login_required
def editStudent(request, id):
    student = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        student.username = username
        student.first_name = first_name
        student.email = email
        student.last_name = last_name

        student.save()
        messages.success(request, "Student Edited Successfully")
        return redirect('student')
    context = {
        'student': student
    }
    return render(request, 'admindashboard/student/edit.html', context)


@login_required
def deleteStudent(request, id):
    student = User.objects.get(id=id)
    student.delete()
    messages.info(request, "Student Deleted Successfully")
    return redirect('student')


@login_required
def room(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, 'admindashboard/room/index.html', context)


@login_required
def addRoom(request):
    if request.method == 'POST':
        room_no = request.POST['roomno']
        building = request.POST['building']
        newroom = Room(
            room_no=room_no,
            building=building
        )
        newroom.save()
        messages.success(request, "Room Added Successfully")
        return redirect('room')

    return render(request, 'admindashboard/room/add.html')


@login_required
def editRoom(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'POST':
        room_no = request.POST['roomno']
        building = request.POST['building']

        room.room_no = room_no
        room.building = building

        room.save()
        messages.success(request, "Room Edited Successfully")
        return redirect('room')
    context = {
        'room': room
    }
    return render(request, 'admindashboard/room/edit.html', context)


@login_required
def deleteRoom(request, id):
    room = Room.objects.get(id=id)
    room.delete()
    messages.info(request, "Room Deleted Successfully")
    return redirect('room')


@login_required
def subject(request):
    subjects = Subject.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, 'admindashboard/subject/index.html', context)


@login_required
def addSubject(request):
    if request.method == 'POST':
        subject_name = request.POST['subjectname']
        newsubject = Subject(
            subject_name=subject_name
        )
        newsubject.save()
        messages.success(request, "Subject Added Successfully")
        return redirect('subject')

    return render(request, 'admindashboard/subject/add.html')


@login_required
def editSubject(request, id):
    subject = Subject.objects.get(id=id)
    if request.method == 'POST':
        subject_name = request.POST['subjectname']
        subject.subject_name = subject_name

        subject.save()
        messages.success(request, "Subject Edited Successfully")
        return redirect('subject')
    context = {
        'subject': subject
    }
    return render(request, 'admindashboard/subject/edit.html', context)


@login_required
def deleteSubject(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.info(request, "Subject Deleted Successfully")
    return redirect('subject')


@login_required
def session(request):
    sessions = Session.objects.all()
    context = {
        "sessions": sessions
    }
    return render(request, 'admindashboard/session/index.html', context)


@login_required
def addSession(request):
    if request.method == 'POST':
        session_date = request.POST['sessiondate']
        start_time = request.POST['starttime']
        end_time = request.POST['endtime']
        room_id = Room.objects.get(id=request.POST['room'])
        subject_id = Subject.objects.get(id=request.POST['subject'])
        teacher_id = User.objects.get(id=request.POST['teacher'])
        attendance_count = 0
        question_answered = 0
        newsession = Session(
            session_date=session_date,
            start_time=start_time,
            end_time=end_time,
            room_id=room_id,
            subject_id=subject_id,
            teacher_id=teacher_id,
            attendance_count=attendance_count,
            question_answered=question_answered
        )
        newsession.save()
        messages.success(request, "Session Added Successfully")
        return redirect('session')
    rooms = Room.objects.all()
    subjects = Subject.objects.all()
    teachers = User.objects.filter(is_staff=True).exclude(
        username="admin").exclude(is_superuser=True)
    context = {
        "rooms": rooms,
        "subjects": subjects,
        "teachers": teachers,
    }
    return render(request, 'admindashboard/session/add.html', context)


@login_required
def editSession(request, id):
    session = Session.objects.get(id=id)
    if request.method == 'POST':
        session_date = request.POST['sessiondate']
        start_time = request.POST['starttime']
        end_time = request.POST['endtime']
        room_id = Room.objects.get(id=request.POST['room'])
        subject_id = Subject.objects.get(id=request.POST['subject'])
        teacher_id = User.objects.get(id=request.POST['teacher'])

        session.session_date = session_date
        session.start_time = start_time
        session.end_time = end_time
        session.room_id = room_id
        session.subject_id = subject_id
        session.teacher_id = teacher_id

        session.save()
        messages.success(request, "Session Edited Successfully")
        return redirect('session')
    rooms = Room.objects.all()
    subjects = Subject.objects.all()
    teachers = User.objects.filter(is_staff=True).exclude(
        username="admin").exclude(is_superuser=True)
    context = {
        "rooms": rooms,
        "subjects": subjects,
        "teachers": teachers,
        'session': session
    }
    return render(request, 'admindashboard/session/edit.html', context)


@login_required
def deleteSession(request, id):
    session = Session.objects.get(id=id)
    session.delete()
    messages.info(request, "Session Deleted Successfully")
    return redirect('session')


@login_required
def question(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, 'admindashboard/question/index.html', context)


@login_required
def addQuestion(request):
    if request.method == 'POST':
        question = request.POST['question']
        user_id = request.user
        session_id = Session.objects.get(id=request.POST["session"])
        newquestion = Question(
            question=question,
            user_id=user_id,
            session_id=session_id

        )
        newquestion.save()
        messages.success(request, "Question Added Successfully")
        return redirect('question')
    sessions = Session.objects.all()
    context = {
        "sessions": sessions
    }
    return render(request, 'admindashboard/question/add.html', context)


@login_required
def editQuestion(request, id):
    selectedQuestion = Question.objects.get(id=id)
    if request.method == 'POST':
        question = request.POST['question']
        session_id = Session.objects.get(id=request.POST["session"])

        selectedQuestion.question = question
        selectedQuestion.session_id = session_id

        selectedQuestion.save()
        messages.success(request, "Question Edited Successfully")
        return redirect('question')
    sessions = Session.objects.all()
    context = {
        "sessions": sessions,
        'question': selectedQuestion
    }
    return render(request, 'admindashboard/question/edit.html', context)


@login_required
def deleteQuestion(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    messages.info(request, "Question Deleted Successfully")
    return redirect('question')


@login_required
def reply(request, id):
    if request.method == "POST":
        reply = request.POST["reply"]
        question = Question.objects.get(id=id)
        teacher = request.user
        newreply = Reply(
            reply=reply,
            question_id=question,
            teacher_id=teacher
        )

        allReplies = Reply.objects.filter(question_id=id).count()
        print(allReplies)
        if allReplies < 1:
            session = Session.objects.get(id=question.session_id.id)
            session.question_answered += 1
            session.save()

        question.end_time = timezone.now()
        question.save()
        time_taken = question.end_time - question.start_time
        newreply.time_taken = time_taken
        newreply.save()

        messages.success(request, "Replied Successfully")
        return redirect('reply', id)
    replies = Reply.objects.filter(question_id=id)
    question = Question.objects.get(id=id)
    context = {
        "replies": replies,
        "question": question
    }
    return render(request, 'admindashboard/reply/index.html', context)


@login_required
def editReply(request, id):
    selectedReply = Reply.objects.get(id=id)
    if request.method == 'POST':
        reply = request.POST['reply']
        selectedReply.reply = reply
        selectedReply.replied_on = timezone.now()

        time_taken = selectedReply.replied_on - selectedReply.question_id.start_time
        selectedReply.time_taken = time_taken
        selectedReply.save()
        messages.success(request, "Reply Edited Successfully")
        return redirect('reply', selectedReply.question_id.id)
    context = {
        'reply': selectedReply
    }
    return render(request, 'admindashboard/reply/edit.html', context)


@login_required
def deleteReply(request, id):
    reply = Reply.objects.get(id=id)
    reply.delete()
    messages.info(request, "Reply Deleted Successfully")
    return redirect('reply', reply.question_id.id)
