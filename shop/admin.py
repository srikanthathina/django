from django.contrib import admin
from .models.product import product
from .models.category import category
from .models.customer import customer

# Register your models here.
class categoryinfo(admin.ModelAdmin):
    list_dispaly=['name']

class productinfo(admin.ModelAdmin):
    list_display=['name','category','price']

class customerinfo(admin.ModelAdmin):
    list_display=['first_name','last_name','email']    


admin.site.register(product,productinfo)
admin.site.register(category,categoryinfo)
admin.site.register(customer,customerinfo)