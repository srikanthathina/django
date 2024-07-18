from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models.product import product
from shop.models.category import category
from django.contrib.auth.hashers import make_password,check_password
from shop.models.customer import customer
from django.views import view

# class based view
class signup(view):
    def get(self,request):
        return render(request,"signup.html")

    def post(self,request):
     fn=request.POST['fn']
     ln=request.POST['ln']
     email=request.POST['email']
     mobile=request.POST['Mobile']
     password=request.POST['Password']
     userdata=[fn,ln,email,mobile,password]
     print(userdata)
     uservalues={
        'fn':fn,
        'ln':ln,
        'email':email,
        'mobile':mobile,
        'password':password
        }
     
     customerdata=customer(first_name=fn,last_name=ln,email=email,mobile=mobile,password=password)

       # Vlidation  
     error_msg=None
     success_msg=None
     if(not fn):
        error_msg="First Name Should Not Be empty"
     elif(not ln):
        error_msg="Last Name Should Not Be empty"
     elif(not email):
        error_msg="Email Field Should Not Be Empty"
     elif(not mobile):
        error_msg="Mobile Field Should Not Be Found"
     elif(not password):
        error_msg="Password Field Should Not Be Found"
     elif(customerdata.isexist()):
        error_msg='Email Already Exists'
     if (not error_msg):
        customerdata.password=make_password(customerdata.password)
        success_msg="Account created successfully"
        customerdata.save()
        msg={'success':success_msg}
        return render (request,'signup.html',msg)  
     else:
         msg={'error':error_msg,'value':uservalues}
         return render (request,'signup.html',msg)
                