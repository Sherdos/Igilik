from django.contrib import admin
from .models import *

# Register your models here.

class SubcategoryInline(admin.TabularInline):
    model=Subcategory
    prepopulated_fields={'slug':('name',)}
    extra=3

class CategoryAdmin(admin.ModelAdmin):
    inlines=[SubcategoryInline]
    prepopulated_fields={'slug':('name',)}


admin.site.register(Order)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory)