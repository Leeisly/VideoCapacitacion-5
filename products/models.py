from django.db import models
from tags.models import Tag

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
        )

    name = models.CharField(max_length=200, null=True) 
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_craeted = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
