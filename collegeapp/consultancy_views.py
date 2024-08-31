from django.shortcuts import render,HttpResponse
from .models import Consultancy
from django.contrib import messages

def registration(request):
    
    if request.method == "GET":

       return render(request,"collegeapp/consultancy/c_registration.html")
    if request.method == "POST":
        con_id=request.POST["con_ID"]
        # print(uname)
        c_pass=request.POST["con_password"]
        c_name=request.POST["c_name"]
        c_phone=request.POST["c_phone"]
        c_mail=request.POST["c_mail"]
        c_desc=request.POST["description"]
        consultancy_obj=Consultancy(c_id=con_id,c_password=c_pass,c_name=c_name,phone=c_phone,email=c_mail,description=c_desc)
        consultancy_obj.save()
        messages.success(request,"Thank you for registration")
    
    return render(request,"collegeapp/consultancy/c_registration.html")