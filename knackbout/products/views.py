from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from products.models import commerce
from .forms import CommerceForm

# Create your views here.
def first(request):
        return render(request,'first.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('first')

def user(request):
    form=CommerceForm
    if request.method=='POST':
        form=CommerceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
        
    return render(request,'user.html',{'form':form})

def products(request):
    dests=commerce.objects.all()
    return render(request,'products.html',{'dests':dests})

#def save_d(request):
    #if request.method=='POST':
        #productname=request.POST['productname']
        #productprice=request.POST['productprice']
        #productimage =request.POST['productimage']
        #productdesc =request.POST['productdesc']
        #offers=request.POST['offers']
        #sv=commerce(productname=productname,productprice=productprice,productimage=productimage,productdesc=productdesc,offers=offers)
        #sv.save()
        #return redirect('/')
    #return redirect('/')