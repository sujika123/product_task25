from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from demoapp.forms import Loginform, Userloginform, productform
from demoapp.models import Product


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form = Loginform()
    form1 = Userloginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        form1 = Userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            tcr = form1.save(commit=False)
            tcr.user = user
            tcr.save()
            return redirect('loginview')
    return render(request,'registration.html',{'form':form,'form1':form1})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)

        if user is not None and user.is_user:
            login(request,user)
            return redirect('userhome')

        else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')

def userhome(request):
    return render(request,'userhome.html')

def add_product(request):
    form = productform()
    u = request.user
    if request.method == 'POST':
        form = productform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('view_product')
    return render(request,'add_product.html',{'form':form})



def view_product(request):
    u = request.user
    data = Product.objects.filter(user=u)
    return render(request, 'view_product.html', {'data': data})


def delete_product(request,id):
    b = Product.objects.get(id=id)
    b.delete()
    return redirect('view_product')


def update_product(request,id):
    user = Product.objects.get(id=id)
    form = productform(instance=user)
    if request.method == "POST":
        form= productform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('view_product')
    return render(request,'update_product.html',{'form':form})

