from bbapp.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.


@login_required
def studentdashboard(request):
    enrollments = request.user.students.count()
    sessions = Session.objects.count()
    questions = Question.objects.filter(user_id=request.user.id).count()
    context = {
        "sessions": sessions,
        "questions": questions,
        "mysubjects": enrollments
    }
    return render(request, 'studentdashboard/index.html', context)


@login_required
def session(request):
    sessions = Session.objects.all()
    student = User.objects.get(id=request.user.id)
    student_course_taken = student.students.all()

    context = {
        "sessions": sessions,
        "student_course_taken": student_course_taken,
    }
    return render(request, 'studentdashboard/session/index.html', context)


@login_required
def enroll(request, id):
    session = Session.objects.get(id=id)
    user = request.user
    session.student.add(user)
    session.attendance_count += 1
    session.save()
    messages.success(request, "Enrolled Successfully")
    return redirect('studentSession')


@login_required
def deleteEnrollment(request, id):
    session = Session.objects.get(id=id)
    user = request.user
    session.student.remove(user)
    session.attendance_count -= 1
    session.save()
    messages.success(request, "Unenrolled Successfully")
    return redirect('studentSession')


@login_required
def question(request):
    questions = Question.objects.exclude(
        user_id=request.user.id).order_by('is_replied')
    context = {
        "questions": questions
    }
    return render(request, 'studentdashboard/question/index.html', context)


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
        return redirect('studentQuestions')
    sessions = Session.objects.all()
    context = {
        "sessions": sessions
    }
    return render(request, 'studentdashboard/question/add.html', context)


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
        return redirect('studentQuestions')
    sessions = Session.objects.all()
    context = {
        "sessions": sessions,
        'question': selectedQuestion
    }
    return render(request, 'studentdashboard/question/edit.html', context)


@login_required
def deleteQuestion(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    messages.info(request, "Question Deleted Successfully")
    return redirect('studentQuestions')


@login_required
def myQuestions(request):
    questions = Question.objects.filter(user_id=request.user.id)
    context = {
        "questions": questions
    }
    return render(request, 'studentdashboard/question/myquestions.html', context)


@login_required
def reply(request, id):
    replies = Reply.objects.filter(question_id=id)
    question = Question.objects.get(id=id)
    context = {
        "replies": replies,
        "question": question
    }
    return render(request, 'studentdashboard/reply/index.html', context)
