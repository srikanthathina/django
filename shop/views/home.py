from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models.product import product
from shop.models.category import category
from django.contrib.auth.hashers import make_password,check_password
from shop.models.customer import customer
from django.views import view


# class based view
class home(view):
    def get(self,request):
        categories=category.objects.all()
        categoryID=request.GET.get('category')
        if categoryID:
         products=product.get_category_id(categoryID)
        else:
          products=product.objects.all()
        data={'products':products,'categories':categories}
        return render(request,'index.html',data)
    def post(self,request):
        pass