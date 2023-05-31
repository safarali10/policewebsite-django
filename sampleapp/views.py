from django.shortcuts import render,redirect
from .models import Signup,Contact,Schedule,Complaint
from django.contrib import messages
# Create your views here.

def police(request):
    return render(request,'police.html')


def form(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        contactnumber=request.POST['contactnumber']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        emailexist=Signup.objects.filter(email=email)
        contactnumberexist=Signup.objects.filter(number=contactnumber)
        if emailexist:
            messages.info(request, 'email already exist')
            return render(request,'registration.html')
        elif contactnumberexist:
            messages.info(request,'contact number already exist')
            return render(request,'registration.html') 
        else:
             Signup(name=name,email=email,address=address,number=contactnumber,password=password,confirmpassword=confirmpassword).save()

    return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        try:
            Signupdetails=Signup.objects.get(name=request.POST['username'],password=request.POST['password'])
            request.session['id']=Signupdetails.name
            request.session['new']=Signupdetails.id
            return redirect('home')
        except Signup.DoesNotExist as e:
            messages.info(request,'invalid username or password')
            return render(request,'login.html')

    return render (request,'login.html')  

def home(request):
    data=request.session['id']
    return render(request,'home.html',{"data":data})

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        Contact(name=name,email=email,subject=subject,message=message).save()
        
    return render(request,'contact.html')

def schedule(request):
    Customer=request.session['new']
    schedules=Schedule.objects.get(user=Customer)
    return render(request,'schedule.html',{"schedules":schedules})
            
def complaint(request):
    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['message']
        Complaint(subject=subject,message=message).save()

    return render(request,'complaint.html')    

def logout(request):
    try:
        del request.session['id']
    except:
        return redirect('/')
    
    
