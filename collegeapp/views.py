from django.shortcuts import render,HttpResponse
from .models import Notice,Course,Employee,Contact,Feedback_Rating,Event
from django.contrib import messages
# Create your views here.
def home(request):
     notice_object_list= Notice.objects.all()
     event_object_list= Event.objects.all()


     notice_context={
     "notice_key":notice_object_list,
     "event_key":event_object_list
     
     }
     return render(request,"collegeapp/html/index.html",notice_context)
def about_us(request):
    notice_object_list= Notice.objects.all()
    notice_context={
    "notice_key":notice_object_list,
    "title":"MyAboutuspage"
    }
    return render(request,"collegeapp/html/about_us.html",notice_context)
def contact_us(request):
    if request.method == "GET":

       return render(request,"collegeapp/html/contact_us.html")
    if request.method == "POST":
        uname=request.POST["username"]#request.POST is a built_in dict
        # print(uname)
        u_mail=request.POST["usermail"]
        u_phone=request.POST["userphone"]
        u_query=request.POST["userquery"]
        contact_obj=Contact(name=uname,email=u_mail,phone=u_phone,user_query=u_query)#object creation of contact
        contact_obj.save()#using ORM concept
        messages.success(request,"Thank you for contacting us we will reach you soon")

    return render(request,"collegeapp/html/contact_us.html")
def feedback(request):
    if request.method == "GET":

       return render(request,"collegeapp/html/feedback.html")
    if request.method == "POST":
        uname=request.POST["username"]
        # print(uname)
        u_mail=request.POST["usermail"]
        u_feedback=request.POST["userfeedback"]
        u_rating=request.POST["rating"]
        feedback_obj=Feedback_Rating(name=uname,email=u_mail,feedback_text=u_feedback,ratings=u_rating)
        feedback_obj.save()
        messages.success(request,"Thank you for Feedback")
    return render(request,"collegeapp/html/feedback.html")
def courses(request):
    course_object_list=Course.objects.all()
    course_dict={
        "course_key":course_object_list
    }
    return render(request,"collegeapp/html/courses.html",course_dict)
def login(request):
    
    return render(request,"collegeapp/html/login.html")
def employee_details(request):
    employee_object_list=Employee.objects.all()
    employee_dict={
        "employee_key":employee_object_list
    }
    return render(request,"collegeapp/html/employee_details.html",employee_dict)
def registration(request):
    return render(request,"collegeapp/html/c_registration.html")


    








































