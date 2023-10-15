import debug_toolbar
from django.urls import include, path
from . import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('dashboard', views.admindashboard, name='admindashboard'),

    path('teacher', views.teacher, name='teacher'),
    path('teacher/add', views.addTeacher, name='addTeacher'),
    path('teacher/edit/<int:id>', views.editTeacher, name='editTeacher'),
    path('teacher/delete/<int:id>', views.deleteTeacher, name='deleteTeacher'),

    path('student', views.student, name='student'),
    path('student/add', views.addStudent, name='addStudent'),
    path('student/edit/<int:id>', views.editStudent, name='editStudent'),
    path('student/delete/<int:id>', views.deleteStudent, name='deleteStudent'),

    path('room', views.room, name='room'),
    path('room/add', views.addRoom, name='addRoom'),
    path('room/edit/<int:id>', views.editRoom, name='editRoom'),
    path('room/delete/<int:id>', views.deleteRoom, name='deleteRoom'),

    path('subject', views.subject, name='subject'),
    path('subject/add', views.addSubject, name='addSubject'),
    path('subject/edit/<int:id>', views.editSubject, name='editSubject'),
    path('subject/delete/<int:id>', views.deleteSubject, name='deleteSubject'),

    path('session', views.session, name='session'),
    path('session/add', views.addSession, name='addSession'),
    path('session/edit/<int:id>', views.editSession, name='editSession'),
    path('session/delete/<int:id>', views.deleteSession, name='deleteSession'),

    path('question', views.question, name='question'),
    path('question/add', views.addQuestion, name='addQuestion'),
    path('question/edit/<int:id>', views.editQuestion, name='editQuestion'),
    path('question/delete/<int:id>', views.deleteQuestion, name='deleteQuestion'),

    path('question/reply/<int:id>', views.reply, name='reply'),
    path('question/reply/edit/<int:id>', views.editReply, name='editReply'),
    path('question/reply/delete/<int:id>',
         views.deleteReply, name='deleteReply'),

]
