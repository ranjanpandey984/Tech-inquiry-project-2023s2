from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bbapp.models import *
# Create your views here.


@login_required
def tutordashboard(request):
    mysubjects = Subject.objects.filter(user_id=request.user.id).count()
    sessions = Session.objects.count()
    questions = Question.objects.exclude(user_id=request.user.id).count()
    context = {
        "sessions": sessions,
        "questions": questions,
        "mysubjects": mysubjects
    }
    return render(request, 'tutordashboard/index.html', context)


@login_required
def session(request):
    sessions = Session.objects.all()
    context = {
        "sessions": sessions
    }
    return render(request, 'tutordashboard/session/index.html', context)


@login_required
def question(request):
    questions = Question.objects.exclude(
        user_id=request.user.id).order_by('is_replied')
    context = {
        "questions": questions
    }
    return render(request, 'tutordashboard/question/index.html', context)


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
        return redirect('myQuestions')
    sessions = Session.objects.all()
    context = {
        "sessions": sessions
    }
    return render(request, 'tutordashboard/question/add.html', context)


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
        return redirect('myQuestions')
    sessions = Session.objects.all()
    context = {
        "sessions": sessions,
        'question': selectedQuestion
    }
    return render(request, 'tutordashboard/question/edit.html', context)


@login_required
def deleteQuestion(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    messages.info(request, "Question Deleted Successfully")
    return redirect('myQuestions')


@login_required
def myQuestions(request):
    questions = Question.objects.filter(user_id=request.user.id)
    context = {
        "questions": questions
    }
    return render(request, 'tutordashboard/question/myquestions.html', context)


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
            question.is_replied = True
            session = Session.objects.get(id=question.session_id.id)
            session.question_answered += 1
            session.save()
        question.is_replied = True
        question.end_time = timezone.now()
        question.save()
        time_taken = question.end_time - question.start_time
        newreply.time_taken = time_taken
        newreply.save()

        messages.success(request, "Replied Successfully")
        return redirect('tutorReply', id)
    replies = Reply.objects.filter(question_id=id)
    question = Question.objects.get(id=id)
    context = {
        "replies": replies,
        "question": question
    }
    return render(request, 'tutordashboard/reply/index.html', context)


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
        return redirect('tutorReply', selectedReply.question_id.id)
    context = {
        'reply': selectedReply
    }
    return render(request, 'tutordashboard/reply/edit.html', context)


@login_required
def deleteReply(request, id):
    reply = Reply.objects.get(id=id)
    reply.delete()
    messages.info(request, "Reply Deleted Successfully")
    return redirect('tutorReply', reply.question_id.id)


@login_required
def mySubject(request):
    subjects = Subject.objects.filter(user_id=request.user)
    context = {
        "subjects": subjects
    }
    return render(request, 'tutordashboard/mysubject/index.html', context)


@login_required
def addMySubject(request):
    if request.method == 'POST':
        subject = Subject.objects.get(id=request.POST['subject'])
        user_id = request.user
        subject.user_id.add(user_id)
        subject.save()
        messages.success(request, "My Subject Added Successfully")
        return redirect('mySubject')
    subjects = Subject.objects.exclude(user_id=request.user)
    context = {
        "subjects": subjects
    }
    return render(request, 'tutordashboard/mysubject/add.html', context)


@login_required
def deleteMySubject(request, id):
    subject = Subject.objects.get(id=id)
    user = request.user
    subject.user_id.remove(user)
    messages.info(request, "My Subject Deleted Successfully")
    return redirect("mySubject")
