from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Color, Size, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "price", "image_preview")
    filter_horizontal = ("category", "colors", "sizes")  # віджети для M2M
    raw_id_fields = ('category', 'colors', 'sizes')  # ключове для уникнення "InvalidCursorName"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="70" height="70" style="object-fit: cover;" />',
                obj.image.url
            )
        return "Немає фото"

    image_preview.short_description = "Фото"


admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)