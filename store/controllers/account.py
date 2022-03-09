from django.http import JsonResponse
from django.shortcuts import redirect, render
from store.form import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store.models import About, Cart, Category, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from store.form import *



@login_required(login_url = 'login')
def accountInfo(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if request.method == 'POST':
            form.save()
            messages.success(request, "Update Successfully!" )
            return redirect('/account')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {
        'item': Product.objects.all()[:4],
        'category': Category.objects.all(),
        'cart': Cart.objects.all(),
        'form':form,
        'about': About.objects.all().first,
    }
    return render(request,'store/account/editaccount.html',context)


@login_required(login_url = 'login')
def deleteAccount(request):
    
    User.objects.get(username= request.user).delete()
    messages.success(request, "Account Deleted Successfully!" )
    return redirect("/")



