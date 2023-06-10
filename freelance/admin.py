from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(Order)
admin.site.register(Media)
admin.site.register(Category,CategoryAdmin)