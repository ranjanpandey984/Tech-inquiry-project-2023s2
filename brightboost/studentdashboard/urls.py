import debug_toolbar
from django.urls import include, path
from . import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('dashboard', views.studentdashboard, name='studentdashboard'),

    path('session', views.session, name='studentSession'),

    path('session/enroll/<int:id>', views.enroll, name='enroll'),
    path('session/enroll/delete/<int:id>',
         views.deleteEnrollment, name='deleteEnrollment'),

    path('question/allquestions', views.question, name='studentQuestion'),
    path('question/add', views.addQuestion, name='studentAddQuestion'),
    path('question/edit/<int:id>', views.editQuestion, name='studentEditQuestion'),
    path('question/delete/<int:id>', views.deleteQuestion,
         name='studentDeleteQuestion'),

    path('question/reply/<int:id>', views.reply, name='studentReply'),

    path('question/myquestions', views.myQuestions, name='studentQuestions'),

]
