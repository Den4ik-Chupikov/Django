from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm, LoginForm

def blogs(request):
    return HttpResponse("Blogs")

def about(request):
    return HttpResponse("About")

def create(request):
    return render(request, "create.html")

def update(request, txt):
    return HttpResponse("Update")

def delete(request, txt):
    return HttpResponse("Delete")

def profile(request, txt):
    return HttpResponse("Profile")

def change_password(request):
    return HttpResponse("Change Password")

def register(request):
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        form = LoginForm()
        if form.is_valid():
            return render(request, 'form_was_valid.html')
    else:
        form = LoginForm()   
    return render(request, "login.html", {"form":form})

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

# Обработка формы на валидность и возврат к начальной форме
def form_view(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'forms/form_was_valid.html')
    else:
        form = MyForm()    
        
    return render(request, 'forms/form.html', {'form': form})

