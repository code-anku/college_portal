from django.shortcuts import render,redirect,HttpResponse
from .models import Student,Student_Feedback_Rating
from django.contrib import messages
from django.views import View
def show_home(request):
    st_id=request.session["student_key"]# fetching the value from dictionary
    print(st_id)
    student_obj=Student.objects.get(student_id=st_id)#fetch a single object
    student_dict={"student_data":student_obj}#binding student object in dict
   # print(student_data.name)
    print(student_obj)

    return render(request,"collegeapp/student/student_home.html",student_dict)
#class based viwes for 
class Login(View):
   def get(self,request):
       return render(request,"collegeapp/html/login.html")
   def post(self,request):
      s_id=request.POST["userID"]
      s_pass=request.POST["userpassword"]#another way to fetch data from dict
       # print(s_id,s_pass)
      msg=self.check_length(s_pass)
      # msg_dict={"error_message":msg}
      if msg:
        messages.error(request,msg)
        return render(request,'collegeapp/html/login.html')
      else:
          student_list= Student.objects.filter(student_id=s_id,student_password=s_pass)

          length=len(student_list) 
          if length>0:
              request.session["student_key"]=s_id#bind student id in session
            #request.session["role"]="student"
              return redirect("student_home")# it is used to redirect the request on the specified url
           # return render(request,'collegeapp/student/student_home.html')
          else:
            messages.error(request,"invalid Credentials")
            return render(request,'collegeapp/html/login.html')
      
   def check_length(self,password):
        if len(password)<=5:
           return "must be greater then 5 characters" 
   

#def login(request):
#     if request.method == "GET":
#        return render(request,"collegeapp/html/login.html")
#     if request.method == "POST":
#         s_id=request.POST["userID"]
#         s_pass=request.POST["userpassword"]#another way to fetch data from dict
#        # print(s_id,s_pass)
#         student_list= Student.objects.filter(student_id=s_id,student_password=s_pass)
#  # select * from student where student_id=s_id and student_password=s_pass
#         length=len(student_list) 
#         if length>0:
#             request.session["student_key"]=s_id#bind student id in session
#             #request.session["role"]="student"
#             return redirect("student_home")# it is used to redirect the request on the specified url
#            # return render(request,'collegeapp/student/student_home.html')
#         else:
#             messages.error(request,"invalid Credentials")
#             return render(request,'collegeapp/html/login.html')
# logout function
def logout(request):
    del request.session["student_key"]
    return redirect("login")
def student_edit_profile(request):
    if request.method =="GET":
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)
        student_dict={"student_data":student_obj}
        return render(request,'collegeapp/student/student_editprofile.html',student_dict)
    if request.method =="POST":
        em=request.POST["usermail"]
        ph=request.POST["userphone"]
        add=request.POST["useraddress"]
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)
        student_obj.email=em
        student_obj.phone=ph
        student_obj.address=add
        student_obj.save()
        student_dict={"student_data":student_obj}
        return render(request,'collegeapp/student/student_feedback.html',student_dict)

def Feedback_Rating(request):
    if request.method =="GET":
      return render(request,'collegeapp/student/student_feedback.html')
    if request.method =="POST":
      s_id=request.session["student_key"]
      student_obj=Student.objects.get(student_id=s_id)
      rt=request.POST["rating"]
      fb=request.POST["feedback"]
     
      s_dict={
          "student_data":student_obj
      }
      messages.info(request,"you have already given feedback")
      return render(request,'collegeapp/student/student_home.html',s_dict)
    else:
      sfr=Student_Feedback_Rating(student=student_obj,ratings=rt,feedback_text=fb)
    #   sfr=Student_Feedback_Rating.objects.filter(student=student_obj,ratings=rt,feedback_text=fb)

      sfr.save()
    #   messages.success(request,"Thank you for feedback")
    #   #message
    return render(request,'collegeapp/student/student_feedback.html')
        


