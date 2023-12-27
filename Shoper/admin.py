#from django.contrib import admin

# # Register your models here.
# from .models import (
#     Categories,
#     SubCategories,
#     Product,
    
# )

from django.contrib import admin
from SubCategory.models import SubCategories
from Category.models import Categories
from Shoper.models import Product



@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
     list_display =['id', 'name']
    
    
@admin.register(SubCategories)
class SubCategoriesModelAdmin(admin.ModelAdmin):
     list_display =['id', 'name','cat_id']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
     list_display =['id', 'title','selling_price','discount_price','basi_description','details_description','stock','tag', 'brand','sub_cat_id','product_1_image','product_2_image','product_3_image','product_4_image']
