from django.contrib import admin
from django.utils.html import format_html
from products.models.department import Department
from products.models.category import Category
from products.models.brand import Brand
from products.models.store import Store
from products.models.product_metadata import ProductMetadata
from products.models.campaign import Campaign
from products.models.shop_look import ShopLook
from products.models.similar_product import SimilarProduct
from products.models.vtov_product import VtovProduct
from products.models.recommended_product import RecommendedProduct


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', )


class ProductMetadataAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin_custom.js',)

    fields = (('department', 'category', 'brand'),
              ('title', 'store', 'redirect_url'),
              ('price', 'description'),
              ('thumbnail_image', 'main_image'),
              ('thumbnail_image_view', 'main_image_view'))

    readonly_fields = ('thumbnail_image_view', 'main_image_view')

    list_display = ('title', 'department', 'category', 'brand',
                    'store', 'redirect_url_view', 'thumbnail_image_view')

    def redirect_url_view(self, obj):
        return format_html('<a href="{0}" target="_blank">{0}</a>'.format(obj.redirect_url))

    def thumbnail_image_view(self, obj):
        return format_html('<img src="{}" width="auto" height="70px" />'.format(obj.thumbnail_image.url))
    thumbnail_image_view.short_description = 'Thumbnail Image'

    def main_image_view(self, obj):
        return format_html('<img src="{}" width="auto" height="70px" />'.format(obj.main_image.url))
    main_image_view.short_description = 'Main Image'


class CampaignAdmin(admin.ModelAdmin):
    pass


class ShopLookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand)
admin.site.register(Store)
admin.site.register(Department)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductMetadata, ProductMetadataAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(ShopLook, ShopLookAdmin)
admin.site.register(SimilarProduct)
admin.site.register(VtovProduct)
admin.site.register(RecommendedProduct)
