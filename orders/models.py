from django.db import models
from products.models import Product

class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Out for delivery'),
            ('Delivered', 'Delivered'),
            )

    
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)   

# Create your models here.
