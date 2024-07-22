from django.contrib import admin

# Register your models here.
from core.models import AllProducts, Category


class AllProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']


admin.site.register(AllProducts,AllProductAdmin)

admin.site.register(Category)