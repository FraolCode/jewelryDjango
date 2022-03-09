
from django.urls import path
from .import views
from store.controllers import authview,cart,checkout,order,contactus,blog,review,account

urlpatterns = [
    path('',views.home,name = 'home'),
    path('shop',views.shop,name = 'shop'),
    path('blog/<str:type>',views.blog,name = 'blog'),
    path('search',views.search,name = 'search'),
    path('searchproduct',views.searchproduct,name = 'searchproduct'),
    path('shop/category/<int:cate_id>',views.searchbycategory,name = 'searchbycategory'),
    path('shop/stock/<str:stock>',views.searchbystock,name = 'searchbystock'),
    
    path('detail/<int:pk>/<str:pro_cate>', views.detail, name='detail'),

    path('categorySearch/<int:pk>', views.shop, name='categorySearch'),

    

    path('register/', authview.register, name = 'register' ),
    path('login/', authview.loginpage, name = 'login' ),
    path('logout/', authview.logoutpage, name = 'logout' ),

    path('add-to-cart',cart.addtocart, name= 'addtocart'),
    path('viewcart',views.cart , name= 'viewcart'),
    path('update-cart',cart.updatecart , name= 'updatecart'),
    path('delete-cart-item',cart.deletecartItem , name= 'deletecartItem'),


    path('checkout',views.checkout , name= 'checkout'),
    path('place-order',checkout.placeorder , name= 'placeorder'),
    
    path('account',views.account,name = 'account'),
    path('editaccount',account.accountInfo,name = 'editaccount'),
    path('deleteaccount',account.deleteAccount,name = 'deleteaccount'),
    


    path('view_order',order.vieworder,name = 'vieworder'),
    path('view_order_items/<str:t_no>',order.vieworderitems,name = 'vieworderitems'),


    path('contactus',views.contactus,name = 'contactus'),
    path('add-contactus',contactus.addcontact , name= 'addcontact'),

    path('blogdiscdetail/<int:pk>', blog.discount, name='blogdiscdetail'),
    path('blogdetail/<int:pk>', blog.post, name='blogdetail'),

    path('add-review',review.addreview , name= 'addreview'),


    path('tmp',views.tmp , name= 'tmp'),
]