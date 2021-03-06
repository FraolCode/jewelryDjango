

from multiprocessing import context
from telnetlib import LOGOUT
from urllib.request import Request
from django.shortcuts import redirect, render
from store.form import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from store.models import Cart, Category, Product
cata = Category.objects.all()
recent = Product.objects.all().order_by('created_at')[:3]
def register(request):
    form = CustomUserForm
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "registered Successfully! Login to Continue" )
            return redirect('/login')
    context = {'form':form,
    
        'item': Product.objects.all()[:4],
        'category': cata,
        'cart': Cart.objects.all(),
        'recent':recent,
        
        
        
    }
    return render(request , 'store/auth/register.html', context )

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passWd = request.POST.get('password')

            user = authenticate(request, username = name, password = passWd)

            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("home")
            else:
                messages.error(request,"Invalid Username / Password")
                return redirect("/login")
        context = {
            'item': Product.objects.all()[:4],
            'category': cata,
            'cart': Cart.objects.all(),
            'recent':recent,
        }
        return render(request , 'store/auth/login.html',context )

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out in Successfully " )
        return redirect('/')
    else:
        return redirect('/')