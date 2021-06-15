from django.contrib import admin
from .models import manufacturing_tracker,style_code,Product
class manufacturing_trackerAdmin(admin.ModelAdmin):
    list_display = ['id','order_placed_date', 'client_name']
class style_codeAdmin(admin.ModelAdmin):
    list_display = ['prd_id','style_code', 'product_name','status','expected_delivery_date']
class Product_Admin(admin.ModelAdmin):
    list_display = ['pid','product_name', 'is_vote','is_home','style_code']
admin.site.register(manufacturing_tracker,manufacturing_trackerAdmin)
admin.site.register(style_code,style_codeAdmin)
admin.site.register(Product,Product_Admin)

# Register your models here.
admin.site.site_header = "CAM Admin"
admin.site.site_title = "CAM Admin Panel"
admin.site.index_title = "Welcome To CAM Admin Panel"