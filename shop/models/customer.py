from django.db import models

# create your models here
class customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=200)

    # checking if email is existing or not
    def isexist(self):
        if customer.objects.filter(email=self.email):
            return True
        return False
    @staticmethod
    def getemail(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False