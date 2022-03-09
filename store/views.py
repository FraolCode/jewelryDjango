
from itertools import count
from multiprocessing import context
from sre_parse import State
from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
cata = Category.objects.all()
pro = Product.objects.all()

            





def home(request):
    total_price = 0
    slider1 = Product.objects.order_by('?')[0]
    slider2 = Product.objects.order_by('?')[0]
    slider3 = Product.objects.order_by('?')[0]
    special_product =  Product.objects.all()[:6]
    trending_item = Product.objects.filter(trending = True)[:6]
    discount = DiscountEvent.objects.all()[:6]

    if request.user.is_authenticated:
        cartItem = Cart.objects.filter(user = request.user)
        
        for item in cartItem:
            total_price = total_price + item.product.selling_price * item.product_qty
    
    context = {
        'slider1':slider1,
        'slider2':slider2,
        'slider3':slider3,
        'special_product':special_product,
        'category': cata,
        'trending_item':trending_item,
        'item': Product.objects.all(),
        'Disblog': DiscountEvent.objects.order_by('?')[:3],
        'blog': Event.objects.order_by('?')[:3],
        'about': About.objects.all().first,
        
        'cart': Cart.objects.all(),
        'total_price':total_price,
        'discount':discount,
        'designers':Designer.objects.all()

        
    }
    return render(request, 'store/index.html',context)
def shop(request):
    instock= 0
    outstock = 0
    Item_l = Product.objects.exclude(quantity = 0)
    for it in Item_l:
        instock = instock + 1
    Item_l = Product.objects.filter(quantity = 0)
    for it in Item_l:
        outstock = outstock + 1
    total_price = 0
    Item_list = Product.objects.exclude(quantity = 0)
    recent = Product.objects.all().order_by('created_at')[:3]
    if request.user.is_authenticated:
        cartItem = Cart.objects.filter(user = request.user)
        
        for item in cartItem:
            total_price = total_price + item.product.selling_price * item.product_qty


    
        

    all = Product.objects.all()
    count = 0
    for proCount in all:
        count = count + 1

    paginator = Paginator(Item_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'blogs': Event.objects.all()[:4],
        'discount': DiscountEvent.objects.all()[:4],
        'item': Product.objects.all()[:4],
        'recent':recent,
        'count':count,
        'category': cata,
        'cart': Cart.objects.all(),
        'total_price':total_price,
        'instock':instock,
        'outstock': outstock,
        'about': About.objects.all().first,
        
    }
    return render(request, 'store/product/shop.html',context)
def blog(request,type):
    
        

    total_price = 0
    if request.user.is_authenticated:
        cartItem = Cart.objects.filter(user = request.user)
        
        for item in cartItem:
            total_price = total_price + item.product.selling_price * item.product_qty
    context = {
        'blogs': Event.objects.all(),
         'discountEvent': DiscountEvent.objects.all(),
        
        'item': Product.objects.all()[:4],
        'category': cata,
        'cart': Cart.objects.all(),
        'total_price':total_price,
        'type':type,
        'about': About.objects.all().first,
    }
    return render(request, 'store/Blog/blog.html',context)

@login_required(login_url = 'login')
def cart(request):
    userprofile = User.objects.filter(id = request.user.id).first()
    cart = Cart.objects.filter(user=request.user)
    cart_count = 0
    for car in cart:
        cart_count = cart_count + 1
    recent = Product.objects.all().order_by('created_at')[:3]
    cartItem = Cart.objects.filter(user = request.user)
    total_price = 0
    for item in cartItem:
        total_price = total_price + item.product.selling_price * item.product_qty

   
    
    context = {
        'cart':cart,
        'recent':recent,
        'carts': cart,
        'category': cata,
        'total_price':total_price,
        'item': Product.objects.all()[:4],
        'cartcount':cart_count,
        'about': About.objects.all().first,
        }
    
    return render(request,"store/cart.html",context)

@login_required(login_url = 'login')
def checkout(request):
    fromCart = Cart.objects.filter(user = request.user)
    cart_count = 0
    
    for car in fromCart:
        cart_count = cart_count + 1
    for item in fromCart:
        if item.product_qty > item.product.quantity:
            
            Cart.objects.filter(pk=item.pk).delete()
            
    cartItem = Cart.objects.filter(user = request.user)
    total_price = 0
    for item in cartItem:
        total_price = total_price + item.product.selling_price * item.product_qty
    
    userprofile = Profile.objects.filter(user = request.user).first



    context = {
        'cartItem':cartItem,
        'total_price':total_price,
        'userprofile':userprofile,
        'cartcount':cart_count,
        'category': cata,
        'item': Product.objects.all()[:4],
        'carts': fromCart,
        'about': About.objects.all().first,
        
    }
    return render(request,"store/checkout.html",context)



def search(request):
    instock= 0
    outstock = 0
    Item_l = Product.objects.exclude(quantity = 0)
    for it in Item_l:
        instock = instock + 1
    Item_l = Product.objects.filter(quantity = 0)
    for it in Item_l:
        outstock = outstock + 1
    if request.method == 'POST':
        searched = request.POST.get('q')
        if searched == '':
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            products = Product.objects.filter(name__contains=searched).first()

            if products:
                return redirect('detail/'+ str(products.id) +'/'+products.category.name)
            else:
                messages.info(request,'No Product matched your search')
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))
def searchproduct(request):
    products = Product.objects.filter(status=0).values_list('name',flat=True)
    productList = list(products)

    return JsonResponse(productList,safe = False)

def searchbycategory(request,cate_id):
    
    total_price = 0
    Item_list = Product.objects.filter(category = cate_id).exclude(quantity = 0)
    recent = Product.objects.all().order_by('created_at')[:3]
    if request.user.is_authenticated:
        cartItem = Cart.objects.filter(user = request.user)
        
        for item in cartItem:
            total_price = total_price + item.product.selling_price * item.product_qty


    instock= 0
    outstock = 0
    Item_l = Product.objects.exclude(quantity = 0)
    for it in Item_l:
        instock = instock + 1
    Item_l = Product.objects.filter(quantity = 0)
    for it in Item_l:
        outstock = outstock + 1

    all = Product.objects.all()
    count = 0
    for proCount in all:
        count = count + 1

    paginator = Paginator(Item_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'blogs': Event.objects.all()[:4],
        'discount': DiscountEvent.objects.all()[:4],
        'item': Product.objects.all()[:4],
        'recent':recent,
        'count':count,
        'category': cata,
        'cart': Cart.objects.all(),
        'total_price':total_price,
        'instock':instock,
        'outstock': outstock,
        'about': About.objects.all().first,
        
    }
    return render(request, 'store/product/shop.html',context)


def searchbystock(request,stock):
    total_price = 0
    recent = Product.objects.all().order_by('created_at')[:3]
    if request.user.is_authenticated:
        cartItem = Cart.objects.filter(user = request.user)
        
        for item in cartItem:
            total_price = total_price + item.product.selling_price * item.product_qty
    instock = 0
    outstock = 0
    Item_l = Product.objects.exclude(quantity = 0)
    for it in Item_l:
        instock = instock + 1
    Item_l = Product.objects.filter(quantity = 0)
    for it in Item_l:
        outstock = outstock + 1
    
    if stock == 'in':
        Item_list = Product.objects.exclude(quantity = 0)
        
    else:
        Item_list = Product.objects.filter(quantity = 0)
        

    all = Product.objects.all()
    count = 0
    for proCount in all:
        count = count + 1

    paginator = Paginator(Item_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'blogs': Event.objects.all()[:4],
        'discount': DiscountEvent.objects.all()[:4],
        'item': Product.objects.all()[:4],
        'recent':recent,
        'count':count,
        'category': cata,
        'cart': Cart.objects.all(),
        'total_price':total_price,
        'instock':instock,
        'outstock': outstock,
        'about': About.objects.all().first,
        
    }
    return render(request, 'store/product/shop.html',context)



def detail(request, pk,pro_cate):
    total_price = 0
    comment_counter = 0
    review = Review.objects.filter(post = pk)
    review_count = 0
    for reviews in review:
        review_count = review_count + 1
    if request.user.is_authenticated:
        cartItem = Cart.objects.filter(user = request.user)
        comment = Review.objects.filter(user = request.user)
        
        
        for item in cartItem:
            total_price = total_price + item.product.selling_price * item.product_qty
        for comments in comment:
            comment_counter = comment_counter + 1

    
    if(Category.objects.filter(name=pro_cate,status = 0)):
        if(Product.objects.filter(pk=pk,status = 0)):
            ItemDetail= Product.objects.filter(pk=pk,status = 0).first()
            rev = Review.objects.filter(post = ItemDetail)
            context = {'ItemDetail':ItemDetail,
            'review':rev,
            'cart': Cart.objects.all(),
            'total_price':total_price,
            'category': cata,
            'item': Product.objects.all()[:4],
            'cart': Cart.objects.all(),
            'comCount': comment_counter,
            'about': About.objects.all().first,
            'review_count':review_count,
            
            }

        else:
            messages.error(request, "No such category found" )
            return redirect('shop')
    else:
        messages.error(request, "No such category found" )
        return redirect('shop')

    
    
    return render(request, 'store/product/product-detail.html',context)

@login_required(login_url = 'login')
def account(request):
    total_price = 0
    if request.user.is_authenticated:
        cartItem = Cart.objects.filter(user = request.user)
        
        for item in cartItem:
            total_price = total_price + item.product.selling_price * item.product_qty
    order = Order.objects.filter(user = request.user)

    context = {
        'order':order,
        'item': Product.objects.all()[:4],
        'cart': Cart.objects.all(),
        'category': cata,
        'item': Product.objects.all()[:4],
        'total_price':total_price,
        'about': About.objects.all().first,
    }
    return render(request, 'store/account/account.html',context)


def tmp(request):
    return render(request,"store/tmp.html")


@login_required(login_url = 'login')
def contactus(request):
    total_price = 0
    order = Order.objects.filter(user = request.user)
    if request.user.is_authenticated:
        cartItem = Cart.objects.filter(user = request.user)
        
        for item in cartItem:
            total_price = total_price + item.product.selling_price * item.product_qty
    userprofile = Profile.objects.filter(user = request.user).first
    context = {
        'userprofile':userprofile,
        'item': Product.objects.all()[:4],
        'category': cata,
        'cart': Cart.objects.all(),
        
        'total_price':total_price,
        'order':order,
        'about': About.objects.all().first,
    }
    return render(request,'store/contactus.html',context)