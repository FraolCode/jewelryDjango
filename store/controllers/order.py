
from django.shortcuts import render


from store.models import About, Category, Order, OrderItem, Product, Profile
cata = Category.objects.all()

def vieworder(request):
    order = Order.objects.filter(user = request.user)
    orderitems = OrderItem.objects.filter(order=order)
    
    context = {
         'orders':order,
         'item': Product.objects.all()[:4],
         'orderitems' : orderitems,
         'category': cata,
         'about': About.objects.all().first,
         
    }
    return render(request, 'store/order/view.html',context)


def vieworderitems(requast,t_no):
    order = Order.objects.filter(traking_no = t_no).filter(user = requast.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    profile = Profile.objects.filter(user = requast.user).first()
    context = {
         'order':order,
         'orderitems': orderitems,
         'profile':profile,
    }
    return render(requast, 'store/order/detailOrder.html',context)

