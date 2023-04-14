from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from eduapp.models import course,addstud,teacheruser
import os

# Create your views here.
def home(request):
    return render(request,'home.html')
def sign(request):
    courses=course.objects.all()
    return render(request,'signup.html',{'course':courses})
def backin(request):
    return render(request,'home.html')
@login_required(login_url='home')

def alogin(request):
    return render(request,'adminlogin.html')
@login_required(login_url='home')
   
def addcourse(request):
    return render(request,'addcourse.html')
def create(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        age=request.POST['age']
        ad=request.POST['adrs']
        email=request.POST['mail']
        num=request.POST['phone']
        username=request.POST['uname']
        password=request.POST['pass']
        rpassword=request.POST['pass1']
        img=request.FILES.get('pic')
        if request.FILES.get('pic') is not None:
            img=request.FILES.get('pic')
        else:
            img="/static/images/default.jpg"
        sel=request.POST['subject']
        course1=course.objects.get(id=sel)
        if password==rpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This username already exist!!!!")
                return redirect('sign')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password )
                user.save()
                u=User.objects.get(id=user.id)
                teacher=teacheruser(address=ad,age=age,number=num,image=img,user=u,course=course1)
                teacher.save()
                return redirect('/')
        else:
            messages.info(request,"password doesnot match...!")
            print("Password is not matching")
            return redirect('sign')
        return redirect('home')
    else:
        return render(request,'signup.html')
def log(request):
    if request.method=='POST':
        usernme=request.POST['user']
        password=request.POST['pass']
        print(password)
        user=auth.authenticate(username=usernme,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.info(request,f'welcome admin')
                return redirect('alogin')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'welcome {usernme}')
                return redirect('tlogin')
        else:
            messages.info(request,'invalid username or password.Try again!!')
            return redirect('home')
    else:
        return render(request,'home.html')
def super(request):
    return render(request,'adminlogin.html')
@login_required(login_url='home')

def addc(request):
    if request.method=='POST':
        coursename=request.POST['cname']
        fees=request.POST['fee']
        stud=course(coursename=coursename,fees=fees)
        stud.save()
        return redirect('alogin')
@login_required(login_url='home')

def addings(request):
    courses=course.objects.all()
    return render(request,'student.html',{'course':courses})
@login_required(login_url='home')

def add(request):
    sname=request.POST['name']
    age=request.POST['age']
    ad=request.POST['adrs']
    joind=request.POST['join']
    mobilenum=request.POST['num']
    sel=request.POST['subject']
    course1=course.objects.get(id=sel)
    stud=addstud(name=sname,age=age,address=ad,joining_date=joind,phone_no=mobilenum,course=course1)
    stud.save()
    return redirect('alogin')
@login_required(login_url='home')

def showdetails(request):
    stud=addstud.objects.all()
    return render(request,'show.html',{'student':stud})
@login_required(login_url='home')

def editpage(request,id):
    edits=addstud.objects.get(id=id)
    editc=course.objects.all()
    return render(request,'edit.html',{'edit':edits,'course':editc})
@login_required(login_url='home')

def editdetails(request,id):
    if request.method=='POST':
        stud=addstud.objects.get(id=id)

        stud.name=request.POST['name']
        stud.address=request.POST['adrs']
        stud.age=request.POST['age']
        stud.joining_date=request.POST['join']
        stud.phone_no=request.POST['num']

        stud.save()
        return redirect('showdetails')
    return render(request,'edit.html')
def delete(request,id):
    stud=addstud.objects.get(id=id)
    stud.delete()
    return redirect('showdetails')
@login_required(login_url='home')

def super(request):
    return render(request,'adminlogin.html')
@login_required(login_url='home')
def logout(request):
    auth.logout(request)
    return redirect('home')
@login_required(login_url='home')

def tlogin(request):
    return render(request,'teachlogin.html')
@login_required(login_url='home')
def seeprofile(request):
    user_id=request.user.id
    see=teacheruser.objects.get(user=user_id)
    return render(request,'showteach.html',{'sp':see})
@login_required(login_url='home')

def teacher(request):
    see=teacheruser.objects.all()
    return render(request,'adminshowteach.html',{'show':see})
@login_required(login_url='home')

def deladmin(request,id):
    tea=teacheruser.objects.get(user=id)
    us=User.objects.get(id=id)
    tea.delete()
    us.delete()
    return redirect('teacher')
@login_required(login_url='home')
def teachedit(request):
    current_user=request.user.id
    print(current_user)
    user1=teacheruser.objects.get(user_id=current_user)
    user2=User.objects.get(id=current_user)
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(user1.image)>0:
                os.remove(user1.image.path)
            user1.image=request.FILES.get('pic')
        user2.first_name=request.POST['fname']
        user2.last_name=request.POST['lname']
        user2.username=request.POST['uname']
        user2.email=request.POST['mail']
        user1.age=request.POST['age']
        user1.address=request.POST['adrs']
        user1.number=request.POST['phone']
        user1.save()
        user2.save()
        return redirect('seeprofile')
    return render(request,'editteacher.html',{'users':user1})






