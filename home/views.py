from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import  login as auth_login
from django.contrib.auth import  logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.
def login(request):
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
        #username should be under 10 characters
        if len(username) > 10:
            messages.error(request,"username must be under 10 characters")
            return redirect('registration')
        #username should be alphanumeric
        if not username.isalnum():
            messages.error(request,"username should contain only letters and numbers")
            return redirect('registration')
        # if confirm password is not same
        if pass1!=pass2:
            messages.error(request,"passwords do not match")
            return redirect('registration')
        #create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been successfully created!!")
        return redirect('login')

    return render(request,'registration.html')