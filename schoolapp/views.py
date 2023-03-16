
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here.

def index(request):
    return render(request,"index.html")



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']



    return render(request,"login.html")




def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']

        if password == cpassword:
            return redirect('login')

    return render(request,"register.html")


def newslatteremail():
    pass


def newpage(request):
    return render(request,"newpage.html")

def form(request):
    if request.method=='POST':
        Name=request.POST['Name']
        DOB=request.POST['DOB']
        AGE=request.POST['AGE']
        GENDER=request.POST['GENDER']
        PHONE_NUMBER=request.POST['PHONE_NUMBER']
        MAIL_id=request.POST['MAIL_id']
        ADDRESS=request.POST['ADDRESS']
        Department=request.POST['Department']

        # if request.POST:
        #         messages.info(request,'Order Confirmed')

        # if 'submit' in request.POST:
        #     messages.info(request, 'Order Confirmed.')

    return render(request,"form.html")