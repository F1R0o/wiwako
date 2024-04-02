from django.contrib import admin
from .models import Category, Wiwako

# Register your models here.



@admin.register(Wiwako)
class WiwakoAdmin(admin.ModelAdmin):
    list_display = ['saxeli_qartulad', 'saxeli_inglisurad', 'category', 'maragshia', 'fasi']
    list_filter = ['category', 'maragshia']
    search_fields = ['saxeli_qartulad', 'saxeli_inglisurad']
    list_per_page = 20



admin.site.register(Category)