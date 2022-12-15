from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from .models import *
import os
import random
import string
from django.conf import settings
from django.core.mail import send_mail
import hashlib
from .serializers import *

def blogdetails(request):
    return render(request,"blog-details.html")

def blog(request):
    return render(request,"blog.html")

def checkout(request):
    # for getting user-data
    if request.session.has_key("user_id"):
        uid=request.session['user_id']
        data=register_tb.objects.filter(id=uid)
        cart_db=cart.objects.filter(UID=uid,STATUS="pending")
        total=0
        for x in cart_db:
            price=x.TOTAL_PRICE
            total=int(price)+total
        return render(request,"checkout.html",{"user":data,"datakey":cart_db,"total":total})
    
    else:
        return render(request,"checkout.html")

def shipping(request):
    if  request.method=="POST":
      same_address=request.POST('same') 
      diff_address=request.POST('diff')
      amount=request.POST('amount')
      # check= 
      # if check:

def payment_gateway(request):
    if request.session.has_key("user_id"):
        uid=request.session['user_id']
        data=cart.objects.filter(UID=uid,STATUS="pending")
        total=0
        for x in data:
            price=x.TOTAL_PRICE
            total=int(price)+total
        return render(request,"payment_gateway.html",{"user":data,'datakey':data,"total":total})
    


def contact(request):
    return render(request,"contact.html")

def index(request):
    data=product.objects.all()
    return render(request,"index.html",{'datakey':data})

def shopdetails(request):
    prdid=request.GET['pid']
    data=product.objects.filter(id=prdid)
    for x in data:
        cat=x.CATEGORY
    category=product.objects.filter(CATEGORY=cat)[:4]

    return render(request,"shop-details.html",{'datakey':data,'related':category})



def shopdetails_page(request):
    data=product.objects.all()
    return render(request,"shopdetails_page.html",{'datakey':data})


    
def shopgrid(request):
    category=product.objects.raw('SELECT * FROM agroapp_product GROUP BY CATEGORY')
    if request.method == "POST":
        cat=request.POST['category']
        if cat == "All":
            data=product.objects.all()
            return render(request,"shop-grid.html",{'datakey':data,'category':category,"cat":cat})
        else:
            data=product.objects.filter(CATEGORY=cat)
            return render(request,"shop-grid.html",{'datakey':data,'category':category,"cat":cat})

    else:
        data=product.objects.all()
        return render(request,"shop-grid.html",{'datakey':data,'category':category})

# def view(request):
#     print("hello")
#     a=request.GET.get('p')
#     # b=product.objects.filter(CATEGORY=a)
#     # for x in b:
#     #     v=x.PRODUCT_NAME
#     #     w=x.PRICE
#     #     y=x.IMAGE
#     #     z=x.id
#         # u=x.Address
#     # dat={"aa":v,"bb":w,"cc":y,"dd":z}

#     print(dat)
#     return JsonResponse(dat)    

def shopingcart(request):
    if request.session.has_key("user_id"):
        uid=request.session['user_id']
        data=cart.objects.filter(UID=uid,STATUS="pending")
        total=0
        for x in data:
            price=x.TOTAL_PRICE
            total=int(price)+total
        return render(request,"shoping-cart.html",{'datakey':data,"total":total})
    else:
        return render(request,"loginandregister.html")




def register(request):
     if  request.method=="POST":
        Name=request.POST['username']
        Email=request.POST['email']
        Phone=request.POST['phone']
        Password=request.POST['password']
        hashpass=hashlib.md5(Password.encode('utf8')).hexdigest()
        check=register_tb.objects.filter(EMAIL=Email)
        if check:
            return render(request,"loginandregister.html",{"error":"Already saved"})
        else:
            add=register_tb(NAME=Name,EMAIL=Email,PHONE=Phone,PASSWORD=Password,hashpass=hashpass)
            add.save()
            x = ''.join(random.choices(Name + string.digits, k=8))
            y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
            subject = 'welcome to Organi store'
            message = f'Hi {Name}, thank you for registering in Organi store. Your user username: {Email} and  password: {Password}. '
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [Email, ] 
            send_mail( subject, message, email_from, recipient_list ) 

            return render(request,"loginandregister.html",{"msg":"Account created"})
     else:
         return render(request,"loginandregister.html")




def login(request):
    if request.method == 'POST':
        Email=request.POST['loginemail']
        Password=request.POST['loginpassword']
        hashpass=hashlib.md5(Password.encode('utf8')).hexdigest()


        data = register_tb.objects.filter(EMAIL=Email,PASSWORD=Password,hashpass=hashpass) #checking email&pass
        if data:
            for x in data:
                status=x.STATUS                
                if status == '1':
                    request.session['user_id'] = x.id
                    request.session['user_name'] = x.NAME
                
                    return render(request,"index.html",{"msg":"Login Sucessfull"})
                else:
                    return render(request,"index.html",{"error":"admin rejected you contact admin for more details"})

        else:
            return render(request,"index.html",{"error":"Password Error"})
    else:
        return render(request, 'loginandregister.html')





def logout(request):
    if request.session.has_key('user_id'):
        del request.session['user_id']
        del request.session['user_name']
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')




def userprofile(request):
    if request.session.has_key("user_id"):
        uid=request.session['user_id']
        data=register_tb.objects.filter(id=uid)
        return render(request,"userprofile.html",{"user":data})
    else:
        return render(request,"loginandregister.html")




def editprofile(request):
    if request.session.has_key("user_id"):
        uid=request.session['user_id']
        data=register_tb.objects.filter(id=uid)
        return render(request,"editprofile.html",{"user":data})
    else:
        return render(request,"editprofile.html")




def updateprofile(request):
    if request.method == 'POST':
        Name=request.POST['username']
        Email=request.POST['email']
        Phone=request.POST['phone']
        currentpass=request.POST['currentpass']
        Password=request.POST['newpassword']
        confPassword=request.POST['confpassword']
        ADDRESS=request.POST['address']
        uid=request.GET['uid']
        check=register_tb.objects.filter(id=uid)
        data=register_tb.objects.filter(id=uid)
        hashpass=hashlib.md5(Password.encode('utf8')).hexdigest()


        if check:
            for x in check:
                pas=x.PASSWORD
        if pas == currentpass:
            if Password == confPassword:
                update=register_tb.objects.filter(id=uid).update(NAME=Name,EMAIL=Email,PHONE=Phone,ADDRESS=ADDRESS,PASSWORD=Password,hashpass=hashpass)
                return HttpResponseRedirect('/userprofile/')
            else:
                return render(request,"editprofile.html",{"user":data,'error':"Password doesnot match"})
        else:
            return render(request,"editprofile.html",{"user":data,'error':"old password doesnot match"})


    else:
        uid=request.session['user_id']
        data=register_tb.objects.filter(id=uid)
        return render(request,"editprofile.html",{"user":data})




def admin_index(request):
    return render(request,"admin/admin_index.html")




def admin_login(request):
    if request.method=="POST":
        Password=request.POST['password']
        Email=request.POST['email']
        check=User.objects.filter(email=Email,password=Password)
        if check:
            for x in check:
                request.session["adminuid"]=x.id
                request.session["adminuid"]=x.id
                request.session["adminemail"]=x.email
            return render(request,"admin/admin_index.html",{})
        else:
            return render(request,"admin/admin_login.html",{})
    else:
        return render(request,"admin/admin_login.html")




def admin_logout(request):
    if request.session.has_key('adminuid'):
        del request.session['adminuid']
        del request.session['adminemail']
        return HttpResponseRedirect('/admin_login/')
    else:
        return HttpResponseRedirect('/adminlogin/')



def admin_userdetails(request):
    query=register_tb.objects.all()
    return render(request,"admin/admin_userdetails.html",{"users":query})



def admin_approve_user(request):
    # if request.session.has_key("user_id"):
    uid=request.GET['uid']
    data=register_tb.objects.filter(id=uid).update(STATUS="1")
    return HttpResponseRedirect("/admin_userdetails/")



def admin_reject_user(request):
    uid=request.GET['uid']
    data=register_tb.objects.filter(id=uid).update(STATUS="0")
    return HttpResponseRedirect("/admin_userdetails/")


def admin_product(request):
    if request.method=="POST":
        product_name=request.POST['product_name']
        product_category=request.POST['category']
        product_description=request.POST['product_description']
        price=request.POST['price']
        quantity=request.POST['quantity']
        IMAGE=request.FILES['img']
        add=product(PRODUCT_NAME=product_name,CATEGORY=product_category,PRICE=price,IMAGE=IMAGE,PRODUCT_DESCRIPTION=product_description)
        add.save()
        return render(request,"admin/admin_product.html",)
    else:
         return render(request,"admin/admin_product.html")


def admin_productdetails(request):
    query=product.objects.all()
    return render(request,"admin/admin_productdetails.html",{"prd":query})


def admin_approve_product(request):
    product_id=request.GET['pid']
    data=product.objects.filter(id=product_id).update(STATUS="1")
    return HttpResponseRedirect("/admin_productdetails/")

def admin_reject_product(request):
    product_id=request.GET['pid']
    data=product.objects.filter(id=product_id).update(STATUS="0")
    return HttpResponseRedirect("/admin_productdetails/")


def admin_productdetails_update(request):
    if request.method=="POST":
        product_name=request.POST['product_name']
        product_category=request.POST['category']
        product_description=request.POST['product_description']
        price=request.POST['price']
        quantity=request.POST['quantity']

        product_id=request.GET['pid']
        img=request.POST['imgs']
        if img == 'yes':
            IMAGEs=request.FILES['img']
            old=product.objects.filter(id=product_id)
            new=product.objects.get(id=product_id)
            for x in old:
                imageurl=x.IMAGE.url
                pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print('Successfully deleted')
            new.IMAGE=IMAGEs
            new.save()
        add=product.objects.filter(id=product_id).update(PRODUCT_NAME=product_name,CATEGORY=product_category,PRICE=price,PRODUCT_DESCRIPTION=product_description,QUANTITY=quantity)
        return HttpResponseRedirect("/admin_productdetails/")
    else:
        product_id=request.GET['pid']
        data=product.objects.filter(id=product_id)
        return  render(request,"admin/admin_productdetails_update.html",{"prd":data})



def admin_productdetails_delete(request):
    product_id=request.GET['pid']
    old=product.objects.filter(id=product_id)            
    for x in old:
        imageurl=x.IMAGE.url
        pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
        if os.path.exists(pathtoimage):
            os.remove(pathtoimage)
    delete=product.objects.all().filter(id=product_id).delete()
    return HttpResponseRedirect("/admin_productdetails/")




def update_profile_pic(request):
    if request.method=="POST":
        userid=request.session['user_id']
        IMAGEs=request.FILES['img']
        old=register_tb.objects.filter(id=userid)
        new=register_tb.objects.get(id=userid)
        for x in old:
            if x.IMAGE:
                imageurl=x.IMAGE.url
                pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imageurl
                if os.path.exists(pathtoimage):
                    os.remove(pathtoimage)
                    print('Successfully deleted')
        new.IMAGE=IMAGEs
        new.save()
    
    return HttpResponseRedirect("/editprofile/")


    # return render(request,"update_profile_pic.html")


def add_to_cart(request):
    if request.method=="POST":
        prdid=request.GET['pid']
        data=product.objects.filter(id=prdid)
        for x in data:
            unitprice=x.PRICE

        product_id=product.objects.get(id=prdid)
        quantity=request.POST['quantity']
        total_price=int(unitprice)*int(quantity)
    
        uid=request.session['user_id']
        userid=register_tb.objects.get(id=uid)
        
        add_to_cart=cart(PID=product_id,UID=userid,TOTAL_PRICE=total_price,QUANTITY=quantity)
        add_to_cart.save()

        return HttpResponseRedirect("/shopingcart/")

    else:
        prdid=request.GET['pid']
        data=product.objects.filter(id=prdid)
        for x in data:
            cat=x.CATEGORY
            category=product.objects.filter(CATEGORY=cat)[:4]

            return render(request,"shop-details.html",{'datakey':data,'related':category})

def remove_from_cart(request):
    prdid=request.GET['eid']
    query=cart.objects.all().filter(id=prdid).delete()
    return HttpResponseRedirect('/shopingcart/')



def addcart(request):
    prdid=request.GET['pid']
    data=product.objects.filter(id=prdid)
    for x in data:
        unitprice=x.PRICE

    product_id=product.objects.get(id=prdid)
    quantity=1
    total_price=int(unitprice)*int(quantity)
    if request.session.has_key("user_id"):
        userid=register_tb.objects.get(id=uid)
        add_to_cart=cart(PID=product_id,UID=userid,TOTAL_PRICE=total_price,QUANTITY=quantity)
        add_to_cart.save()
        return HttpResponseRedirect("/shopingcart/")
    
    else:
        return render(request, 'loginandregister.html')





def ajview(request):
    
    cat=request.GET.get('cat')
    print(cat,"********")
    if cat == "all":
        prd=product.objects.all()
        print(prd)
        # return JsonResponse(prd,safe=False)  
        # farmer = farmer_register.objects.all()
        product_serializer = productSerializer(prd, many=True)
        return JsonResponse(product_serializer.data, safe=False)
    else:
        prd=product.objects.filter(CATEGORY=cat)
    # for x in b:
    #     v=x.Fullname
    #     w=x.Email
    #     y=x.Place
    #     z=x.Phone
    #     u=x.Address
    # dat={"aa":v,"bb":w,"cc":y,"dd":z,"ee":u}
        print(prd)
        # return JsonResponse(prd,safe=False)  
        # farmer = farmer_register.objects.all()
        product_serializer = productSerializer(prd, many=True)
        return JsonResponse(product_serializer.data, safe=False)  