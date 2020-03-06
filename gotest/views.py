from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Essay2


def index(request):
    return render(request,'index.html')

def starttest(request):
    return render(request,"starttest.html")

def index1(request):
    if request.method=="POST":
        q1=request.POST['q1']
        q2=request.POST['q2']
        q3=request.POST['q3']
        q4=request.POST['q4']
        q5=request.POST['q5']
        q6=request.POST['q6']
        q7=request.POST['q7']
        q8=request.POST['q8']
        q9=request.POST['q9']
        q10=request.POST['q10']

        essay=Essay2(q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6,q7=q7,q8=q8,q9=q9,q10=q10)
        essay.save()
        return render(request,"index.html")
    else:
        return render(request,"starttest.html")
    