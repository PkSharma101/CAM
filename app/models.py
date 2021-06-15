from django.db import models
import uuid
import datetime
from django.utils.crypto import get_random_string
from time import *
import random
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class manufacturing_tracker(models.Model):
    id = models.CharField(max_length=6,primary_key=True,editable=False)
    def save(self, *args, **kwargs):
        if not self.id:
            milli_sec=time()*1000
            self.id =''.join(random.sample(get_random_string(3)+str(milli_sec).split('.')[0][-3:],6))
            
        return super(manufacturing_tracker, self).save(*args, **kwargs)
    order_placed_date = models.DateField()
    client_name = models.CharField(max_length=100,default="")
    def __str__(self):
        return str(self.id)

class style_code(models.Model):
    prd_id= models.ForeignKey(manufacturing_tracker, on_delete=models.CASCADE)
    style_code = models.CharField(max_length=100,default="")
    product_name = models.CharField(max_length=100,default="")
    status = models.CharField(max_length=256, choices=[('fabric inhouse', 'fabric inhouse'), ('cutting', 'cutting'),('printing and labelling','printing and labelling'),('stitching', 'stitching'),('ironing packing', 'ironing packing'),('quality check','quality check'),('shipped','shipped'),],default="")
    image=models.ImageField(upload_to="image/",default='')
    expected_delivery_date = models.DateField(default=datetime.datetime.now)
    def __str__(self):
        return str(self.prd_id)

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    product_name = models.CharField(default="",max_length=20)
    is_vote = models.BooleanField(default=False,null=True,blank=True)
    is_home = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(upload_to="image/",default='')
    color = models.CharField(default="",max_length=15)
    style_code = models.CharField(default="",max_length=15)
    like_count = models.IntegerField(null=True,blank=True,default=0)
    dislike_count = models.IntegerField(null=True,blank=True,default=0)
    category = models.CharField(max_length=256, choices=[('tshirts', 'tshirts'), ('shirts', 'shirts'), ('jeans', 'jeans')],default="")
    size_available = models.CharField(max_length=256, choices=[('S', 'S'), ('M', 'M'),('L','L'),('XL', 'XL'),('XXL', 'XXL'),('XXXL','XXXL'),],default="")
    pdetails = models.CharField(max_length=500,default="")
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return str(self.prd_id)