
from distutils.log import error
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from sympy import O
from .models import login_user, upload_image,product,category,order
from django.contrib.auth.hashers import make_password, check_password
import datetime
# Create your views here.


def home(request):
    request.session["cartcheck"]=0

    if request.method=="POST":
        request.session["cartcheck"]=1
        product_id = request.POST.get('cartid')
        remove=request.POST.get('minus')
        cart_id= request.session.get('cart')
        if cart_id:
            quantity=cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id]=quantity-1
                else:
                    cart_id[product_id] = quantity + 1
            else:
                cart_id[product_id]=1 
            #cart_id[product_id] = quantity + 1
        else:
            cart_id={}
            cart_id[product_id] = 1
        request.session['cart']=cart_id
        print(request.session['cart'])
    path = product.objects.all()
    cat = category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        path = product.objects.filter(category_id=category_id)
    else:
        path = product.objects.all()
    return render(request,'home.html', {"path": path, "cate": cat})
    
def contact(request):
    fetch_img=upload_image.objects.all()
    return render (request,'contact.html',{"fetch_img": fetch_img})



def log(request):
    error_msg=None
    if request.method == "POST":
        username = request.POST.get('username')
        passw = request.POST.get('passw')
        print(username,passw)
        try:
            fetch_email=login_user.objects.get(username=username)
            if fetch_email:
                error_msg="Alerady exist"
                return render(request,"home.html",{"error_msg":error_msg})
        except:
            contact=login_user(username=username, passw=make_password(passw))
            contact.save()
            return HttpResponseRedirect("contact/")
    return render(request,'home')

def cart(request):
    if request.session["cartcheck"]==1:
        ids=list(request.session.get("cart").keys())
        cart_pro=product.objects.filter(id__in = ids)
        print(cart_pro)
        return render(request,"cart.html",{'cart_pro':cart_pro})
    else:
        return render(request,"cart.html")
    # if request.method=="POST":
    #     if request.session.username:
    #         ids=list(request.session.get("cart").keys())
    #         cart_pro=product.objects.filter(id__in = ids)
    #         print(cart_pro)
    #         return render(request,"cart.html",{'cart_pro':cart_pro})
    # else:
    #     return render(request, "home.html")
def sign_in(request):
    error_msg=None
    if request.method=="POST":
        email=request.POST.get("username2")
        pssd=request.POST.get("passw2")
        print(email)
        print(pssd)
        try:
            fetch_email=login_user.objects.get(username=email)

            # fetch_email=login_user.objects.get(passw1=pssd)
            if (fetch_email.username==email):
                
                flag = check_password(pssd, fetch_email.passw)
                if flag:
                    request.session['email'] = fetch_email.username
                    request.session['customer_id']=fetch_email.id
                    return render(request,'home.html',{'fetch_email.username': fetch_email.username })
                else:
                    error_msg = "Please Enter valid password"
                    return render(request, 'home.html', {'error_msg': error_msg})
        except:
            error_msg = "Please Enter valid  Email"
            return redirect("home")
    return HttpResponse(fetch_email.email, fetch_email.passw)


def logout(request):
    request.session.clear()
    print("----------logout Sucssess---------------------")
    return redirect('home')
def checkout(request):
    if request.method=="POST":
        address=request.POST.get("address")
        mobile=request.POST.get("mobile")
        customer_id=request.session.get("customer_id")
        cart=request.session.get("cart")
        products=product.objects.filter(id__in=list(cart.keys()))
        for pro in products:
            save_order_dtls=order(
                customer=login_user(id=customer_id),
                product=pro,
                price=pro.price,
                quantity=cart.get(str(pro.id)),
                address=address,
                phone=mobile,)
            save_order_dtls.save()
            request.session['cart']={}
        return redirect('cart')
def order_dtls(request):
    customer=request.session.get('customer_id')
    orders=order.objects.filter(customer=customer).order_by('-date')
    tp=0
    for i in orders:
        tp=tp+(i.price *i.quantity)
        print(tp)
    return render(request,'order.html',{'orders':orders,"tp":tp})