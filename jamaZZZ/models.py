from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class UserProfile(models.Model):
 NID_LENGTH = 5
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=100)
 # email = models.EmailField(blank=True, null=True)
 nid = models.CharField(max_length=NID_LENGTH,default='12345')  # min length 10
 contact_no = models.CharField(max_length=20, blank=True, null=True, default='+880')

 picture = models.ImageField(upload_to='images/', blank=True, null=True,
                             default='images/Default_pic.jpg')
 about_myself = models.TextField(blank=True, null=True, default='will add later')
 address = models.CharField(max_length=255)

 def __str__(self):
  return self.name



class Items(models.Model):
 id = models.IntegerField(primary_key=True)
 item_name = models.CharField(max_length=200)
 item_description = models.TextField(blank=True, null=True)
 item_pic = models.ImageField(upload_to='images/', null=True, blank=True,default='images/Default_pic.jpg')
 item_price = models.FloatField()
 item_category = models.CharField(max_length=200)
 item_stock = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

 def __str__(self):
    return self.item_name


class ProductWomen(models.Model):
 id = models.IntegerField(primary_key=True)
 product_name = models.CharField(max_length=200)
 product_description = models.TextField(blank=True, null=True)
 product_pic = models.ImageField(upload_to='images/', null=True, blank=True,default='images/Default_pic.jpg')
 product_price = models.FloatField()
 product_category = models.CharField(max_length=200)
 product_stock = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])


 def __str__(self):
    return self.product_name


class Men(models.Model):
 id = models.IntegerField(primary_key=True)
 product_name = models.CharField(max_length=200)
 product_description = models.TextField(blank=True, null=True)
 product_pic = models.ImageField(upload_to='images/', null=True, blank=True,default='images/Default_pic.jpg')
 product_price = models.FloatField()
 product_category = models.CharField(max_length=200)
 product_stock = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
 def __str__(self):
    return self.product_name


class Design(models.Model):
 design_name = models.CharField(max_length=200)
 design_description = models.TextField(blank=True, null=True)
 design_pic = models.ImageField(upload_to='images/', null=True, blank=True,default='images/Default_pic.png')
 design_price = models.FloatField()

 def __str__(self):
    return self.design_name


class Cart(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
 product = models.ForeignKey(Items, on_delete=models.CASCADE, blank=True, null=True)
 quantity = models.PositiveIntegerField(default=1, blank=True, null=True)

 def __str__(self):
  return f"Cart for {self.user}"


class Order(models.Model):


 PAYMENT_CHOICES = [

  ('bkash', 'bkash'),
  ('bank', 'bank'),
  ('nagad', 'nagad'),
  ('COD', 'COD'),
  ('rocket', 'rocket'),

 ]

 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Items, on_delete=models.CASCADE, blank=True, null=True)
 p_quantity = models.PositiveIntegerField(default=1, blank=True, null=True)

 shipping_address = models.TextField(max_length=200)
 payment_method = models.CharField(max_length=30, choices=PAYMENT_CHOICES, default='COD', blank=True, null=True)


 def __str__(self):
  return f"Order {self.id} by {self.user}"
