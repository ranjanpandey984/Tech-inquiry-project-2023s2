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
]
