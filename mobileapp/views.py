from django.shortcuts import render,redirect
from .forms import MobileCreation,Brandadd
from .models import Brand
from.models import Brand,Mobile
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,"home.html")

#mobile functions


def mobile_create(request):
    context={}
    form=MobileCreation()
    context["form"]=form

    if request.method=="POST":
        form=MobileCreation(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"mobile created")

            return redirect("addmobiles")
        else:
            messages.error(request,"mobile can't be added")
            context["form"]=form
            return render(request,"mobile_create.html",context)
    else:
        context["form"]=form
        return render(request,"mobile_create.html",context)

def mobile_list(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"list_mobiles.html",context)


def update_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    form = MobileCreation(instance=mobile)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = MobileCreation(instance=mobile, data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobile")

    return render(request, "updatemobile.html", context)

def removemobile(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("listmobile")

def viewmobile(request,id):
    mobiles=Mobile.objects.get(id=id)
    context={}
    context["mobiles"]=mobiles
    return render(request,"viewmobile.html",context)






#Brand functions

def createbrands(request):
    form=Brandadd()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=Brandadd(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"brand created")
            return redirect("home")
        else:
            messages.error(request,"brand can't be added")
            context["form"]=form
            return render(request,"viewbrands.html",context)
    return render(request,"viewbrands.html",context)

def listbrands(request):
    brands=Brand.objects.all()
    context={}
    context["brands"]=brands
    return render(request,"display.html",context)

def viewbrands(request,id):
    brands=Brand.objects.get(id=id)
    context={}
    context["brands"]=brands
    return render(request,"brandview.html",context)

def remove(request,id):
    brands=Brand.objects.get(id=id)
    brands.delete()
    return redirect("listbrand")

def update(request,id):
    brand=Brand.objects.get(id=id)
    form=Brandadd(instance=brand)
    context={"form":form}
    if request.method=="POST":
        form=Brandadd(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbrand")

    return render(request, "updates.html", context)

