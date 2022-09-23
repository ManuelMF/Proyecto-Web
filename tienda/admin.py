from django.contrib import admin

from .models import CategoriaProdu, Producto

# Register your models here.

class CategoriaProAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProdu, CategoriaProAdmin)
admin.site.register(Producto, ProductoAdmin)
