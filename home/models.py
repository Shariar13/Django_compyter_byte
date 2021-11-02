from django.db import models
from django.db.models.fields.files import ImageField
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.conf import settings 



# post
class front_order(models.Model):
    category=models.CharField(max_length=99)
    username=models.CharField(max_length=99,null=True)
    name=models.CharField(max_length=99)
    phone=models.CharField(max_length=99)
    email=models.CharField(max_length=99)
    address=models.CharField(max_length=99)
    quantity=models.CharField(max_length=99)
    details=models.TextField()
    status=models.CharField(max_length=99,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class back_order(models.Model):
    category=models.CharField(max_length=99)
    username=models.CharField(max_length=99,null=True)
    name=models.CharField(max_length=99)
    phone=models.CharField(max_length=99)
    email=models.CharField(max_length=99)
    address=models.CharField(max_length=99)
    quantity=models.CharField(max_length=99)
    details=models.TextField()
    status=models.CharField(max_length=99,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name

class fullstack_order(models.Model):
    category=models.CharField(max_length=99)
    username=models.CharField(max_length=99,null=True)
    name=models.CharField(max_length=99)
    phone=models.CharField(max_length=99)
    email=models.CharField(max_length=99)
    address=models.CharField(max_length=99)
    quantity=models.CharField(max_length=99)
    details=models.TextField()
    status=models.CharField(max_length=99,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    
    

    def __str__(self):
        if len(self.name)>50:
            return self.name[:50]+"..."
        return self.name
