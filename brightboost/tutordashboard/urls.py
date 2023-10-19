import debug_toolbar
from django.urls import include, path
from . import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('dashboard', views.tutordashboard, name='tutordashboard'),


    path('session', views.session, name='tutorSession'),

    path('question/allquestions', views.question, name='tutorQuestion'),
    path('question/add', views.addQuestion, name='tutorAddQuestion'),
    path('question/edit/<int:id>', views.editQuestion, name='tutorEditQuestion'),
    path('question/delete/<int:id>', views.deleteQuestion,
         name='tutorDeleteQuestion'),

    path('question/reply/<int:id>', views.reply, name='tutorReply'),
    path('question/reply/edit/<int:id>', views.editReply, name='tutorEditReply'),
    path('question/reply/delete/<int:id>',
         views.deleteReply, name='tutorDeleteReply'),

    path('mysubject', views.mySubject, name='mySubject'),
    path('mysubject/add', views.addMySubject, name='addMySubject'),
    path('mysubject/delete/<int:id>',
         views.deleteMySubject, name='deleteMySubject'),

    path('question/myquestions', views.myQuestions, name='myQuestions'),
]
