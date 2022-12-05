from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import *
# Create your views here.
def loginView(request):
    return render(request,"app/login.html")

def homeView(request):
    return render(request,"app/home.html")

def lostView(request):
    return render(request,"app/lost.html")

def foundView(request):
    return render(request,"app/found.html")





def registerView(request):
    return render(request,"app/register.html")


def InsertData(request):
    if request.method=="POST":
        fname=request.POST['fname']
        email=request.POST['email']
        contact=request.POST['contact']
        date=request.POST['date']
        lastseen=request.POST['lastseen']
        desc=request.POST['desc']
      

        newuser=Student.objects.create(Fullname=fname,Email=email,Contact=contact,Lostdate=date,Lastseen=lastseen,Description=desc)

        return redirect('show')

def showPage(request):
    #for fetching all data
    all_data=Student.objects.all()    
    return render(request,"app/show.html",{'key1':all_data})



def UpdateData(request,pk):
    udata= Student.objects.get(id=pk)
    udata.Fullname=request.POST['fname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    udata.Lostdate=request.POST['date']
    udata.Lastseen=request.POST['lastseen']
    udata.Description=request.POST['desc']
    udata.save()
    return redirect('show')

def DeleteData(request,pk):
    ddata=Student.objects.get(id=pk)
    ddata.delete()
    return redirect('lostProfile')

    
def UserRegister(request):
    if request.method == "POST":
        fname=request.POST['fname']
        email=request.POST['email']
        contact=request.POST['contact']
        course=request.POST['course']
        passw=request.POST['passw']
        cpass=request.POST['cpass']

        user= User.objects.filter(Email=email)

        if user:
            message="user already exists"
            return render(request,"app/register.html",{'msg':message})
        else:
            if passw == cpass:
                newuser=User.objects.create(Fullname=fname,Email=email,Contact=contact,Course=course,Password=passw)
                message="user registered successfully"
                return render(request,"app/login.html",{'msg':message})
                
            else:
                message="password and confirm password does not match"
                return render(request,"app/register.html",{'msg':message})


        
def LoginUser(request):
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
    try:
        user=User.objects.get(Email=email)
        if user:
            if user.Password==password:
                request.session['id']=user.id
                request.session['Fullname']=user.Fullname
                request.session['Email']=user.Email
                request.session['Contact']=user.Contact
                request.session['Course']=user.Course
                request.session['Password']=user.Password
                
                return render(request,"app/home.html")
            else:
                message="password does not match"
                return render(request,"app/login.html",{'msg':message})

    except User.DoesNotExist:
        message="user does not exist,please register first"
        return render(request,"app/register.html",{'msg':message})

            
def FoundView(request):
    if request.method=="POST":
        fname=request.POST['fname']
        email=request.POST['email']
        contact=request.POST['contact']
        placefound=request.POST['placefound']
        date=request.POST['date']
        pics=request.FILES['image']

        founddata=Found.objects.create(Fullname=fname,Email=email,Contact=contact,Foundplace=placefound,Foundon=date,Image=pics)
        return redirect('foundshow')

        
def foundshowPage(request):
    #for fetching all data
    all_data=Found.objects.all()   
    return render(request,"app/foundshow.html",{'key1':all_data})        

def EditPage(request,pk):
    get_data=Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})    

def profileView(request):

   
    all_data=User.objects.all().filter(Email=request.session.get('Email'))
    return render(request,"app/profile.html",{'key1':all_data})   

    
def lostProfileView(request):
    all_data=Student.objects.all().filter(Email=request.session.get('Email'))
    if all_data:
        return render(request,"app/lostProfile.html",{'key1':all_data})  
    else:
        message="no record found"
        return render(request,"app/profile.html",{'msg':message})   

def foundProfileView(request):
    all_data=Found.objects.all().filter(Email=request.session.get('Email'))
    if all_data:
        return render(request,"app/foundProfile.html",{'key1':all_data})  
    else:
        message="no record found"
        return render(request,"app/profile.html",{'msg':message})   
   
def logoutRequestView(request):
    logout(request)
    message="Logged out successfully!"
    return render(request,"app/login.html",{'msg':message})

def UpdateFoundData(request,pk):
    udata= Found.objects.get(id=pk)
    udata.Fullname=request.POST['fname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    udata.Foundplace=request.POST['placefound']
    udata.Foundon=request.POST['date']
    udata.Image=request.POST['image']
    udata.save()
    return redirect('foundProfile')

def DeleteFoundData(request,pk):
    ddata=Found.objects.get(id=pk)
    ddata.delete()
    return redirect('foundProfile')

    
def editFoundpage(request,pk):
    get_data=Found.objects.get(id=pk)
    return render(request,"app/editFound.html",{'key2':get_data}) 

def editprofileview(request,pk):
    udata=User.objects.get(id=pk)
    udata.Fullname=request.POST['fname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    udata.Course=request.POST['course']
    udata.Password=request.POST['passw']
    udata.save()
    return redirect('profile')

def editprofilepage(request,pk):
    get_data=User.objects.get(id=pk)
    return render(request,"app/editprofile.html",{'key2':get_data}) 

