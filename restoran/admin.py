from django.contrib import admin


from . models import Order,Product,Category


class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)


admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category,CategoryAdmin)