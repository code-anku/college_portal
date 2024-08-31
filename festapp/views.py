from django.shortcuts import render,HttpResponse

# Create your views here.
def fest_home(request):
    return HttpResponse("<h1>This is college fest home page</h1>")
def about(request):
    return HttpResponse("<h1>This is college fest about page</h1>")
def collegefest(request):
    return HttpResponse("<h1>This is college fest collegefest</h1>")