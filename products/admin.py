from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from products.models.campaign import Campaign
from products.models.category import Category
from products.models.department import Department
from products.models.home_carousel import HomeCarousel
from products.models.merchant import Merchant
from products.models.product import Product
from products.models.recommended_product import RecommendedProduct
from products.models.shop_look import ShopLook
from products.models.similar_product import SimilarProduct
from products.models.sub_category import SubCategory
from products.models.vtov_product import VtovProduct


class MerchantAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name',)


class DepartmentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'department', )
    list_filter = ('department',)
    search_fields = ('name', 'department__name')


class SubCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    class Media:
        js = ('js/admin_category_custom.js',)

    list_display = ('name', 'category', 'department')
    list_filter = ('department', 'category')
    search_fields = ('name', 'department__name', 'category__name')


class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/admin_category_custom.js',)

    list_display = ('title', 'department', 'category', 'subcategory', 'merchant', 'brand', 'color_view',
                    'redirect_url_view', 'price', 'image1_view', 'image2_view')

    list_filter = ('department', 'category',
                   'subcategory', 'merchant', 'brand',)

    search_fields = ('title', 'merchant__name', 'brand',)

    readonly_fields = ('image1_view', 'image2_view')

    def color_view(self, obj):
        return format_html('<span style="color: {0};">{0}</span>'.format(obj.color))
    color_view.short_description = 'Color'

    def redirect_url_view(self, obj):
        return format_html('<a href="{0}" target="_blank">{0}</a>'.format(obj.redirect_url))

    def image1_view(self, obj):
        return format_html('<img src="{}" width="auto" height="70px" />'.format(obj.image1.url))
    image1_view.short_description = 'Image1'

    def image2_view(self, obj):
        return format_html('<img src="{}" width="auto" height="70px" />'.format(obj.image2.url)) if obj.image2 else ''
    image2_view.short_description = 'Image2'


class ShopLookAdmin(SortableAdminMixin, admin.ModelAdmin):
    class Media:
        js = ('js/admin_shoplook_custom.js',)

    list_display = ('title', 'department', 'image_view', 'products_list')
    readonly_fields = ('image_view',)

    def image_view(self, obj):
        return format_html('<img src="{}" width="auto" height="70px" />'.format(obj.image.url))
    image_view.short_description = 'Image'

    def products_list(self, obj):
        return ", ".join([p.title for p in obj.products.all()])


class CampaignAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'products_list')

    def products_list(self, obj):
        return ", ".join([p.title for p in obj.products.all()])


class SimilarProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    class Media:
        js = ('js/admin_products_custom.js',)

    list_display = ('product', 'products_list')

    def products_list(self, obj):
        return ", ".join([p.title for p in obj.similar_products.all()])


class VtovProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    class Media:
        js = ('js/admin_products_custom.js',)

    list_display = ('product', 'products_list')

    def products_list(self, obj):
        return ", ".join([p.title for p in obj.vtov_products.all()])


class RecommendedProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    class Media:
        js = ('js/admin_products_custom.js',)

    list_display = ('product', 'products_list')

    def products_list(self, obj):
        return ", ".join([p.title for p in obj.recommended_products.all()])


class HomeCarouselAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = ('title', 'browse_url_view',
                    'text_color_view', 'image_view',)

    search_fields = ('title', )

    readonly_fields = ('image_view', )

    def text_color_view(self, obj):
        return format_html('<span style="color: {0};">{0}</span>'.format(obj.text_color))
    text_color_view.short_description = 'Text Color'

    def browse_url_view(self, obj):
        return format_html('<a href="{0}" target="_blank">{0}</a>'.format(obj.browse_url))

    def image_view(self, obj):
        return format_html('<img src="{}" width="auto" height="70px" />'.format(obj.image.url))
    image_view.short_description = 'Image'


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(ShopLook, ShopLookAdmin)
admin.site.register(SimilarProduct, SimilarProductAdmin)
admin.site.register(VtovProduct, VtovProductAdmin)
admin.site.register(RecommendedProduct, RecommendedProductAdmin)
admin.site.register(HomeCarousel, HomeCarouselAdmin)
