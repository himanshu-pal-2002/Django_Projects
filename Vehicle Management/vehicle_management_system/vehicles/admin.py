from django.contrib import admin
from .models import Vendor,Product,PurchaseOrder,DeliveryChallan,Vehicle


admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(PurchaseOrder)
admin.site.register(DeliveryChallan)
admin.site.register(Vehicle)



# Register your models here.
