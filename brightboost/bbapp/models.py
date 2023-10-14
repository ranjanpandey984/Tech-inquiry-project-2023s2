from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


# class Student(models.Model):
#     fee = models.FloatField(blank=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.first_name


# class Teacher(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.first_name


# class Subject(models.Model):
#     subject_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.subject_name


# class Room(models.Model):
#     room_no = models.CharField(max_length=50)
#     building = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.room_no} {self.building}"


# class Session(models.Model):
#     session_date = models.DateField()
#     start_time = models.TimeField(auto_now_add=True)
#     end_time = models.TimeField(auto_now_add=True)
#     attendance_count = models.IntegerField()
#     subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
#     room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.session_date} {self.start_time}"


# class Question(models.Model):
#     question = models.TextField()
#     start_time = models.DateTimeField(default=timezone.now)
#     end_time = models.DateTimeField(null=True, default=None)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.question
