from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from .models import Product
from .models import Biding
from .models import Maxamout


def user(request):
    try:
        value = request.session["us_er"]
        data = User.objects.get(email=value)
        return render(request, "welcome.html", {"data": data})
    except:
        return render(request, "user/userlogin.html")


def register(request):
    return render(request, "user/register.html")


def registersucces(request):
    na = request.POST['name']
    pw = request.POST['password']
    co = request.POST['contact']
    em = request.POST['email']
    emg = request.FILES["img"]
    sts = "pending"
    User(name=na, pasw=pw, contact=co, email=em, image=emg, status=sts).save()
    messages.success(request, "Registration is pending wait just a minet ")
    return redirect('register')


def userlogin(request):
    ea = request.POST.get("uemail")
    pa = request.POST.get("upswd")

    try:
        User.objects.get(email=ea, pasw=pa)
        try:
            st = "approved"
            data = User.objects.get(email=ea, status=st)
            request.session["us_er"] = ea
            request.session.set_expiry(1200)
            return render(request, "welcome.html", {"data": data})
        except:
            return render(request, "user/userlogin.html", {"msg": "Your Registration Is Still Pending"})
    except:
        return render(request, "user/userlogin.html", {"msg": "Please Enter Valid Email And Password"})


def log_out(request):
    del request.session["us_er"]
    return redirect('ho_me')


def home_user(request):
    eamail = request.session["us_er"]
    data = User.objects.get(email=eamail)
    return render(request, "welcome.html", {"data": data})


def seller(request):
    eamail = request.session["us_er"]
    data = User.objects.get(email=eamail)
    return render(request, "user/seller.html", {"data": data})


def productadd(request):
    eamail = request.session["us_er"]
    data = User.objects.get(email=eamail)
    return render(request, "user/addproduct.html", {"data": data})


def product(request):
    cata = request.POST.get("c1")
    nam = request.POST.get("n1")
    price = request.POST.get("p1")
    dec = request.POST.get("d1")
    img = request.FILES["img"]
    sta = "not_biding"
    eamail = request.session["us_er"]
    data = User.objects.get(email=eamail)
    id = data.id
    Product(p_name=nam, title=cata, bid_price=price, dics=dec, img=img, p_status=sta, user_id=id).save()
    messages.success(request, "upload successfully")
    return redirect('seller')


def view_product(request):
    email = request.session["us_er"]
    data = User.objects.get(email=email)
    id = data.id
    dataa = Product.objects.filter(user_id=id)
    return render(request, "user/view.html", {"data": data, "dataa": dataa})


def delete_product(request):
    pid = request.GET.get("y")
    Product.objects.get(p_id=pid).delete()
    return redirect('view_product')


def not_biding(request):
    email = request.session["us_er"]
    data = User.objects.get(email=email)
    id = data.id
    st = "not_biding"
    dataa = Product.objects.filter(user_id=id, p_status=st)
    return render(request, "user/not_biding.html", {"dataa": dataa, "data": data})


def biding(request):
    email = request.session["us_er"]
    data = User.objects.get(email=email)
    u_id = data.id
    id = request.GET.get("x")
    Product.objects.filter(p_id=id).update(p_status="biding")
    d1 = Product.objects.get(p_id=id)
    Maxamout(pid_id=id, uid_id=u_id, maxamount=d1.bid_price).save()

    return redirect('not_biding')


def biding_(request):
    email = request.session["us_er"]
    data = User.objects.get(email=email)
    id = data.id
    st = "biding"
    dataa = Product.objects.filter(user_id=id, p_status=st)
    return render(request, "user/not_biding.html", {"dataa1": dataa, "data": data})


def buyer(request):
    email = request.session["us_er"]
    data = User.objects.get(email=email)
    data3 = Maxamout.objects.all()
    return render(request, "user/buyer.html", {"data": data, "data3": data3})


def save_bid(request):
    email = request.session["us_er"]
    data = User.objects.get(email=email)

    id = data.id

    bamount = request.POST.get("p1")

    pid = request.POST.get("p_id")
    Biding(amount=bamount, pid_id=pid, uid_id=id).save()
    m1 = Maxamout.objects.get(pid_id=pid)
    maxa_mount = m1.maxamount
    if float(bamount) > maxa_mount:
        Maxamout.objects.filter(pid_id=pid).update(maxamount=bamount)
        messages.success(request, "Biding Successfully Good Luck")
        return redirect('buyer')
    else:
        messages.error(request, "Bid Amount More Than Product Price")
        return redirect('buyer')


def bid_view(request):
    mail=request.session["us_er"]
    data = User.objects.get(email=mail)
    pid=request.GET.get("x")
    data4=Biding.objects.filter(pid_id=pid)
    return render(request,"user/bidview.html",{"data":data,"data4":data4})