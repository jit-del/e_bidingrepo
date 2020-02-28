from django.shortcuts import render, redirect
from app2.models import Admin
from app1.models import User
from app2.sms import sendSMS

data = None


def adminlogin(request):
    try:
        v1 = request.session["user"]
        data=Admin.objects.get(email=v1)
        return render(request, "welcomeadmin.html", {"data": data})
    except:
         return render(request,"adminlogin.html")

def homepage(request):
    return render(request,"home.html")

def logincheck(request):

    email=request.POST.get("email")
    pswd=request.POST.get("pswd")
    try:
        global data
        data=Admin.objects.get(email=email,password=pswd)

    except:
        return render(request,"adminlogin.html",{"msg":"Plese Enter Valid Email and Password"})
    else:
        request.session["user"]=email
        request.session.set_expiry(1200)
        return render(request, "welcomeadmin.html", {"data": data})


def logout(request):
    del request.session["user"]
    global  data
    data=None
    return redirect('ho_me')



def pending(request):
    global data
    data1=User.objects.filter(status="pending")
    return render(request, "admin/pending.html",{"d1":data1,"data":data})


def approved(request):
    global data
    data2=User.objects.filter(status="approved")
    return render(request,"admin/pending.html",{"d2":data2,"data":data})


def adminapoved(request):
    id=request.GET.get("x")
    qs=User.objects.filter(id=id)
    name=""
    con=""
    for x in qs:
        name=x.name
        con=x.contact
    qs.update(status="approved")

    mess="Hello Mr/Miss: "+name+" . your ragistration is approved"
    x=sendSMS(str(con),mess)
    print(x)
    return redirect('pending')


def admindeclint(request):
    id=request.GET.get("y")
    User.objects.filter(id=id).update(status ="declient")
    return redirect('pending')


def decliend(request):
    global data
    data3=User.objects.filter(status="declient")
    return render(request,"admin/pending.html",{"d3":data3,"data":data})


def admin_declint(request):
    global data
    id=request.GET.get("y")
    User.objects.filter(id=id).update(status="declient")
    return redirect('approved')


def aadmina_prove(request):
    id = request.GET.get("x")
    User.objects.filter(id=id).update(status="approved")
    return redirect('decliend')


def home(request):
    global data
    return render(request,"welcomeadmin.html",{"data":data})


