from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.po_number

class DeliveryChallan(models.Model):
    dc_number = models.CharField(max_length=100)
    purchase_order = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE)

    def __str__(self):
        return self.dc_number

class Vehicle(models.Model):


    vehicle_number = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    purchase_order_number = models.CharField(max_length=50)
    delivery_challan_number = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicle_number

