from django.contrib import admin
from .models import School,Teacher

admin.site.register(School)
admin.site.register(Teacher)

# Register your models here.
admin.site.site_header='Happy New Year'
admin.site.site_title='Khush Raho'
admin.site.index_title='Dhanywad'