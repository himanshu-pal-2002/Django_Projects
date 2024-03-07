from django.db import models

# Create Models for Product Category:

class Product_Category(models.Model):

    Product_category_id = models.IntegerField()
    Product_category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Product_category_name

class Product(models.Model):

    Product_Category = models.ForeignKey(Product_Category,on_delete = models.CASCADE)
    Product_id = models.CharField(max_length=100)
    Product_name = models.CharField(max_length=100)
    Product_brand = models.CharField(max_length=100)

    def __str__(self):
        return self.Product_name