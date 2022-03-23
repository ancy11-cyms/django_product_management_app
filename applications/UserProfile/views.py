from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserInfo

#from .models import User_TB,User

# Create your views here.


def Userregisterview(request):
    userdata = UserRegister(request.POST)
    if userdata.is_valid():
        userdata.save()
        return redirect('Homepage')
    contenxt = {
        'userdata':userdata
    }
    return render(request,"register.html",contenxt)

    

def Homepage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            if user.is_staff and user.is_active:
                request.session['user'] = username
                login(request, user)
                return redirect('dashbord')
            else:
                request.session['user'] = username
                login(request,user)
                return redirect('dashbord')
        else:
            return render(request, "login.html", {'msg': "Invalid Username Or Password"})
    return render(request, "login.html")


def userLogout(request):
    logout(request)
    return redirect('Homepage') 

@login_required(login_url='Homepage')
def dashbord(request):
    return render(request, "UserProfile/home.html")

@login_required(login_url='Homepage')
def About_us(request):
    about_data = UserInfo.objects.filter(User=request.user)
    return render(request, "UserProfile/about.html",{'about_data':about_data})

@login_required(login_url='Homepage')
def Resume(request):
    resume_data = UserInfo.objects.filter(User=request.user)
    print(resume_data)
    return render(request, "UserProfile/resume.html",{'resume_data':resume_data})

@login_required(login_url='Homepage')
def Porfolio(request):
    return render(request, "UserProfile/porfolio.html")

@login_required(login_url='Homepage')
def Blog(request):
    return render(request, "UserProfile/blog.html")

@login_required(login_url='Homepage')
def Contact(request):
    return render(request, "UserProfile/contact.html")

