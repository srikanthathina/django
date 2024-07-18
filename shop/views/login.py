from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models.product import product
from shop.models.category import category
from django.contrib.auth.hashers import make_password,check_password
from shop.models.customer import customer
from django.views import view

# class based view
class login(view):
    def get(self,request):
        return render(request,'login.html')


    def post(self,request):
        email=request.POST['email']
        password=request.POST['password']
        # to check email found or not
        users=customer.getemail(email)
        error_msg=None
        if users:
            # if email found check password
             check=check_password(password,users.password)
            # if password found
             if check:
                return redirect('/')
             
             else:
                  error_msg="Password is incorrect"
                  msg={'error':error_msg}
                  return render(request,'login.html',msg)
        else:
            error_msg="email is incorrect"
            msg={'error':error_msg}
            return render(request,'login.html',msg)
        
        