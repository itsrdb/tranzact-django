from operator import mod
from django.db import models
from pyparsing import empty

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=10, default='xyz')
    email = models.EmailField()

    def __str__(self):
        return self.name

class employees(models.Model):
    name = models.CharField(max_length=50, default='user')
    email = models.EmailField()
    company = models.ForeignKey(company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class invoices(models.Model):
    name = models.CharField(max_length=50, default='abc')
    buyer = models.ForeignKey(company, on_delete=models.CASCADE, related_name='buyer_invoice')
    seller = models.ForeignKey(company, on_delete=models.CASCADE, related_name='seller_invoice')
    product = models.CharField(max_length=200, default='')
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.name