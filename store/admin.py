from django.contrib import admin
from .models import Product
    # ,ProductGallery,ReviewRating,Variation,VariationManager

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','is_available')
    prepopulated_fields = {'slug':('product_name',)}


admin.site.register(Product,ProductAdmin)