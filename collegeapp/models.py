from django.db import models
from django.utils import timezone
# Create your models here.
class Notice(models.Model):
    notice_contents=models.CharField(max_length=45)
    date=models.DateField(default=timezone.now)

    def __str__(self):
     return self.notice_contents 
## Course Model##


class Course(models.Model):
    course_name=models.CharField(max_length=45,primary_key=True)
    course_fees=models.IntegerField()
    course_duration=models.CharField(max_length=40)
    course_contents=models.TextField(blank=True)
    def __str__(self):
       return self.course_name


## contact model##
class Contact(models.Model):
   name=models.CharField(max_length=45)
   email=models.EmailField(max_length=45)
   phone=models.CharField(max_length=10)
   user_query=models.TextField()
   date=models.DateField(default=timezone.now)
   def __str__(self):
      return self.name
   
## Feedback model##

class Feedback_Rating(models.Model):
   name=models.CharField(max_length=45)
   email=models.EmailField(max_length=45)
   feedback_text=models.TextField()
   ratings=models.CharField(max_length=6)
   date=models.DateField(default=timezone.now)
   def __str__(self):
      return self.name


##Employee Model
class Employee(models.Model):
   name=models.CharField(max_length=45)
   email=models.EmailField(max_length=45)
   phone=models.CharField(max_length=10)
   designation=models.CharField(max_length=20)
   employee_pic=models.FileField(max_length=200,upload_to="collegeapp/employee_pic",default="")
   def __str__(self):
      return self.name
   ##Student Model##
gender=[
   ("M","Male"),
   ("F","Female")
]
class Student(models.Model):
   course=models.ForeignKey(Course,on_delete=models.DO_NOTHING)
   name=models.CharField(max_length=45)
   email=models.EmailField(max_length=45)
   phone=models.CharField(max_length=10)
   student_id=models.CharField(max_length=40,primary_key=True)
   student_password=models.CharField(max_length=40)
   gender=models.CharField(max_length=6,choices=gender)
   description=models.TextField()
   address=models.TextField()
   student_pic=models.FileField(max_length=200,upload_to="collegeapp/student_pic",default="")
   def __str__(self):
      return self.name


##Event Model##

class Event(models.Model):
   event_name=models.CharField(max_length=50)
   event_venue=models.CharField(max_length=100)
   event_pic=models.FileField(max_length=100,upload_to="collegeapp/event_pic",default="")
   event_description=models.TextField()
   event_date=models.DateField(default=timezone.now)
   def __str__(self):
      return self.event_name

##Consultancy model##

class Consultancy(models.Model):
   c_id=models.CharField(max_length=45,primary_key=True)
   c_password=models.CharField(max_length=45)
   c_name=models.CharField(max_length=45)
   phone=models.CharField(max_length=45)
   email=models.EmailField(max_length=45)
   description=models.TextField()
   date=models.DateField(default=timezone.now)
   def __str__(self):
      return self.c_name 

##student feedback rating##

class Student_Feedback_Rating(models.Model):
   student=models.OneToOneField(Student,on_delete=models.DO_NOTHING)
   
   feedback_text=models.TextField()
   ratings=models.CharField(max_length=6)
   date=models.DateField(default=timezone.now)
   
 