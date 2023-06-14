from django.shortcuts import render
from django.http import HttpResponse

def blogs(request):
    return HttpResponse("Blogs")

def about(request):
    return HttpResponse("About")

def create(request):
    return HttpResponse("Create")

def update(request, txt):
    return HttpResponse("Update")

def delete(request, txt):
    return HttpResponse("Delete")

def profile(request, txt):
    return HttpResponse("Profile")

def change_password(request):
    return HttpResponse("Change Password")

def register(request):
    return HttpResponse("Register")

def login(request):
    return HttpResponse("Login")

def logout(request):
    return HttpResponse("Logout")

def look_blog(request, txt):
    return HttpResponse("look_blog")

def comment(request, txt):
    return HttpResponse("Comment")

def index(request):
    return render(request, 'index.html')

def extends(request):
    return render(request, 'extends.html')
