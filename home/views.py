from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import  login as auth_login
from django.contrib.auth import  logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.models import Product
# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        loginusername=request.POST['username']
        loginpassword=request.POST['password']
        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            auth_login(request,user)
            messages.success(request,"Successfully logged in as a "+ str(request.user))
            return redirect('index')
        else:
            messages.warning(request,"Invalid credentials please try again")
            return redirect('login')
    else:
        return render(request,'login.html') 

def registration(request):
    if request.method == 'POST':
        #get the user parametrer
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        #check for erroneous input
        #username shouldn't be already existed
        if User.objects.filter(username=username).exists():
            messages.warning(request,"username already exist")
            return redirect('registration')
        # email id should n't exist already
        if User.objects.filter(email=email).exists():
            messages.warning(request,"already registered from this email id")
            return redirect('registration')
        #username should be under 10 characters
        if len(username) > 10:
            messages.warning(request,"username must be under 10 characters")
            return redirect('registration')
        #username should be alphanumeric
        if not username.isalnum():
            messages.warning(request,"username should contain only letters and numbers")
            return redirect('registration')
        # if confirm password is not same
        if pass1!=pass2:
            messages.warning(request,"passwords do not match")
            return redirect('registration')
        #create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been successfully created!!")
        return redirect('login')

    return render(request,'registration.html')

def logout(request):
    auth_logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('login')