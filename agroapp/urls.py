from django.urls import path
from agroapp import views

urlpatterns = [
    path('',views.index),
    path('blog/',views.blog),
    path('blogdetails/',views.blogdetails),
    path('contact/',views.contact),
    path('checkout/',views.checkout),
    path('shop-details/',views.shopdetails),
    path('shopdetails_page/',views.shopdetails_page),
    path('payment_gateway/',views.payment_gateway),


    path('shopgrid/',views.shopgrid),
    path('shopingcart/',views.shopingcart),
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('userprofile/',views.userprofile),
    path('editprofile/',views.editprofile),
    path('updateprofile/',views.updateprofile),

    #admin_panel
    path('admin_index/',views.admin_index),  
    
    path('admin_login/',views.admin_login),
    path('admin_logout/',views.admin_logout),
    
   
    path('admin_userdetails/',views.admin_userdetails),
    path('approve/',views.admin_approve_user),
    path('reject/',views.admin_reject_user),
    
    
    path('admin_product/',views.admin_product),
    path('admin_productdetails/',views.admin_productdetails),
    path('product_approve/',views.admin_approve_product),
    path('product_reject/',views.admin_reject_product),
    path('admin_productdetails_update/',views.admin_productdetails_update),
    path('admin_productdetails_delete/',views.admin_productdetails_delete),
    path('update_profile_pic/',views.update_profile_pic),
    
    path('add_to_cart/',views.add_to_cart),
    path('addcart/',views.addcart),
    
    
    path('remove_from_cart/',views.remove_from_cart),
    # path('view/',views.view),
    

    path('ajview/',views.ajview),
    









    
    
    
    




    
    
]